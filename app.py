import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Marham Labs Scraper", layout="wide")

st.title("🧪 Marham Labs Data Scraper")
st.write("Click the button below to extract lab test data and generate CSV file.")

extract_data_url = "https://www.marham.pk/api/lab/tests-optimized"
required_all_available_labs = "2,3,9,15"
diff_labs = required_all_available_labs.split(",")
#there were only 4 labs at that time we can even fetch all and here we are only using required ids 


if st.button("🚀 Run Scraper"):

    all_records = []

    with st.spinner("Extracting data... Please wait ⏳"):
        try:
            for labs in diff_labs:
                params = {"lab_id": labs}
                response = requests.get(extract_data_url, params=params)

                if response.status_code != 200:
                    st.error("❌ Something went wrong while fetching data.")
                    st.stop()

                data = response.json()
                tests = data.get("lab_tests", [])

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
            st.error(f"⚠ Error occurred: {e}")
            st.stop()

    # Convert to DataFrame
    df = pd.DataFrame(all_records)

    # Save CSV
    df.to_csv("all_labs_tests.csv", index=False)

    # Success message
    st.success(f"✅ File created successfully! Saved {len(df)} records.")

    # Show preview
    st.subheader("📊 Preview of Extracted Data")
    st.dataframe(df, use_container_width=True)

    # Download button
    st.download_button(
        label="📥 Download CSV File",
        data=df.to_csv(index=False),
        file_name="all_labs_tests.csv",
        mime="text/csv"
    )