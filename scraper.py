import requests
import pandas as pd
import sys
import time

extract_data_url = "https://www.marham.pk/api/lab/tests-optimized"
required_all_available_labs = "2,3,9,15,50"
diff_labs = required_all_available_labs.split(",")
#there were only 4 labs at that time we can even fetch all and here we are only using required ids 

all_records = []

# Loading animation setup
loading_text = "Extracting data"
dots = ["   ", ".  ", ".. ", "..."]

for i, labs in enumerate(diff_labs):
    
    # Show loading animation
    sys.stdout.write(f"\r{loading_text} {dots[i % len(dots)]}")
    sys.stdout.flush()
    time.sleep(0.3)

    params = {"lab_id": labs}
    response = requests.get(extract_data_url, params=params)

    if response.status_code != 200:
        print("\nSomething went wrong!")
        break

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

# Save to CSV
df = pd.DataFrame(all_records)
df.to_csv("all_labs_tests.csv", index=False)

# Replace loading line with success message
sys.stdout.write("\r" + " " * 50)  # Clear line
sys.stdout.write(f"\r✅ File created successfully! Saved {len(df)} records to all_labs_tests.csv\n")
sys.stdout.flush()