# 🧪 Marham Labs Test Data Scraper

A powerful and efficient Python scraper designed to extract complete lab test data from Marham Labs directory.

This scraper automatically collects all available lab test information across all labs using pagination and exports the data into a structured CSV file for easy analysis and usage.

---

## 🚀 Features

* ✅ Scrapes **all labs test data**
* ✅ Extracts complete pricing and discount information
* ✅ Saves clean, structured data into **CSV format**
* ✅ Fast and efficient
* ✅ Easy to use and customize
* ✅ Production-ready code structure

---

## 📊 Data Fields Extracted

The scraper extracts the following data points:

| Field Name           | Description                |
| -------------------- | -------------------------- |
| `id`                 | Unique Test ID             |
| `lab_id`             | Unique Lab ID              |
| `lab_name`           | Name of the Lab            |
| `test_name`          | Name of the Test           |
| `test_type`          | Type/category of test      |
| `fee`                | Original Test Fee          |
| `discount`           | Discount amount            |
| `discountPercentage` | Discount percentage        |
| `discountedFee`      | Final price after discount |

---

## 🌐 Source

Data is scraped from:

```
https://www.marham.pk/labs
```

Using Marham's internal API with full pagination support.

---

## 📁 Output

The scraper generates:

```
all_labs_tests.csv
```

Example:

```csv
id,lab_id,lab_name,test_name,test_type,fee,discount,discountPercentage,discountedFee
123,45,Chughtai Lab,CBC Test,Blood,1500,300,20,1200
124,45,Chughtai Lab,LFT Test,Blood,2000,400,20,1600
```

---

## 🛠 Requirements

Install dependencies:

```bash
pip install requests
```

Python version:

```
Python 3.7+
```

---

## ▶️ How to Run

```bash
python scraper.py
```

The script will:

1. Fetch all labs
2. Fetch all tests for each lab
3. Handle pagination automatically
4. Save results into CSV file

---

## ⚙️ How it Works

The scraper uses Marham's optimized API endpoint to fetch lab test data in the format below:

```
https://www.marham.pk/api/lab/tests-optimized?lab_id={id_parm}
https://www.marham.pk/api/lab/tests-optimized?lab_id={id_parm}&page={page_parm}
...
```
When a lab has multiple tests, the API returns data across multiple pages.


## 📦 Example API Response Structure

Data is returned in JSON format like this:

```
{
  "id": 2,
  "name": "Chughtai Lab",
  "lab_tests": [
    {
      "id": 54684,
      "lab_id": 2,
      "name": "1666 GTT / GCT (75 Grams Glucose Tolerance Test (for Pregnant Patient) (Fasting, 75gm Glucose 1 Hour, 2 Hours))",
      "type": "Pathology",
      "fee": 1500,
      "discount": 300,
      "discountPercentage": 20,
      "discountedFee": 1200
    },
    {
      "id": 54864,
      "lab_id": 2,
      "name": "17-OH Progesterone",
      "type": "Pathology",
      "fee": 4000,
      "discount": 800,
      "discountPercentage": 20,
      "discountedFee": 3200
    }
  ]
}
```


### 🧠 Pseudo Flow

```
START

↓
Fetch all labs from:
https://www.marham.pk/labs

↓
Extract lab_id for each lab

↓
FOR each lab_id:

    GET /tests-optimized?lab_id={lab_id}

    ↓
    Read response JSON

    ↓
    Extract:
        lab_id
        lab_name
        lab_tests[]

    ↓
    FOR each test in lab_tests:

        Extract:
            test_id
            test_name
            test_type
            fee
            discount
            discountPercentage
            discountedFee
            lab_id
            lab_name

        ↓
        Save row into CSV file

    END FOR

END FOR

↓
SAVE all data into:
all_labs_tests.csv

↓
END
```

---

It automatically continues until no more data is available.

---

## 📂 Recommended Project Structure

```
Marham-Labs-Scraper/
│
├── scraper.py
├── all_labs_tests.csv
├── README.md
└── requirements.txt
```

---

## 💡 Use Cases

* Data analysis
* Price comparison platforms
* Healthcare analytics
* Research projects
* Automation pipelines

---

## 🧠 Author

**Waqar Jamil**
Data Engineer | Technical Project Manager |  Cloud Data Engineer

## 📫 Connect With Me

- LinkedIn: https://linkedin.com/in/waqar488
- GitHub: https://github.com/waqarjamil480

---

## 📜 License

This project is open-source and free to use for educational and research purposes.

---

## ⭐ Support

If you find this useful, please ⭐ star the repository.
