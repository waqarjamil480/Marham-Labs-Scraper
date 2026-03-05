import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Marham Labs Scraper", layout="wide")

st.title("🧪 Marham Labs Data Scraper")
st.write("Click the button below to extract lab test data and generate CSV file.")

extract_data_url = "https://www.marham.pk/api/lab/tests-optimized"

# Keep labs as STRING
required_all_available_labs = "2,3,9,15,50,51"
#there were only 5 labs at that time we can even fetch all and here we are only using required ids 
# Convert string to list
diff_labs = required_all_available_labs.split(",")

if st.button("🚀 Run Scraper"):

    all_records = []

    with st.spinner("Extracting data... Please wait ⏳"):

        for labs in diff_labs:

            try:
                params = {"lab_id": labs}
                response = requests.get(extract_data_url, params=params, timeout=10)

                if response.status_code != 200:
                    st.warning(f"⚠ Request failed for lab {labs}")
                    continue

                # Safe JSON parsing
                try:
                    data = response.json()
                except ValueError:
                    st.warning(f"⚠ Lab {labs} returned invalid JSON")
                    continue

                tests = data.get("lab_tests", [])

                # Skip labs with no data
                if not tests:
                    st.info(f"ℹ No data found for lab {labs}, skipping...")
                    continue

                for test in tests:
                    all_records.append({
                        "discount": test.get("discount"),
                        "discountPercentage": test.get("discountPercentage"),
                        "discountedFee": test.get("discountedFee"),
                        "fee": test.get("fee"),
                        "id": test.get("id"),
                        "lab_id": test.get("lab_id"),
                        "test_name": test.get("name"),
                        "test_type": test.get("type"),
                        "lab_name": data.get("name")
                    })

            except Exception as e:
                st.warning(f"⚠ Error processing lab {labs}: {e}")
                continue

    df = pd.DataFrame(all_records)

    if df.empty:
        st.error("❌ No data extracted.")
    else:
        df.to_csv("all_labs_tests.csv", index=False)

        st.success(f"✅ File created successfully! Saved {len(df)} records.")

        st.subheader("📊 Preview of Extracted Data")
        st.dataframe(df, use_container_width=True)

        st.download_button(
            label="📥 Download CSV File",
            data=df.to_csv(index=False),
            file_name="all_labs_tests.csv",
            mime="text/csv"
        )