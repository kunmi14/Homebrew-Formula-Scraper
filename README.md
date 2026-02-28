# 🍺 Homebrew Formula Scraper

A Python web scraping project that extracts package information from the **Homebrew Formulae** website and collects installation analytics data via their public API.

This script scrapes package names, versions, descriptions, and installation statistics (30, 90, and 365 days), then saves everything into a structured JSON file.

---

## 📌 Project Overview

This project:

- Scrapes package data from Homebrew
- Extracts:
  - Package name
  - Current version
  - Description
- Fetches analytics data from the Homebrew API:
  - Installations in the last 30 days
  - Installations in the last 90 days
  - Installations in the last 365 days
- Stores all results in a JSON file
- Measures execution time per package and total runtime

---

## 🛠️ Technologies Used

- Python 3
- requests – HTTP requests
- BeautifulSoup (bs4) – HTML parsing
- lxml – HTML parser engine
- json – Data serialization
- time – Performance measurement

---

## 🌐 Data Sources

Formula list page:
https://formulae.brew.sh/formula

Formula API endpoint:
https://formulae.brew.sh/api/formula/{formula_name}.json

---

## 📂 Output Format

The script generates a JSON file structured like this:

```json
[
    {
        "name": "wget",
        "version": "1.21.4",
        "description": "Internet file retriever",
        "analytics": {
            "30d": 123456,
            "90d": 345678,
            "365": 1234567
        }
    }
]
```

---

## 🚀 How It Works

1. Sends a GET request to the Homebrew formula page.
2. Parses the HTML table containing formula data.
3. Iterates through each row.
4. For each formula:
   - Extracts name, version, and description.
   - Sends another request to the Homebrew API.
   - Retrieves installation analytics.
5. Appends structured data to a list.
6. Writes the collected data into a JSON file.
7. Displays performance timing for each formula and total runtime.

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```bash
pip install requests beautifulsoup4 lxml
```

### 2️⃣ Update JSON output path

Modify:

```python
json_path = '/your/path/output.json'
```

### 3️⃣ Run the script

```bash
python scraper.py
```

---

## ⚡ Performance Features

- Uses time.perf_counter() for precise timing.
- Measures:
  - Individual formula processing time
  - Total execution time
- Gracefully skips formulas with HTTP or JSON errors.

---

## 🧠 What This Project Demonstrates

- Web scraping with BeautifulSoup
- Working with REST APIs
- JSON data handling
- Error handling with try/except
- Performance measurement
- Nested dictionary parsing
- Clean data structuring

---

## 📈 Possible Improvements

- Add concurrency with asyncio or concurrent.futures for faster API calls
- Store results in a database (PostgreSQL / SQLite)
- Add CLI arguments for dynamic file paths
- Implement logging instead of print statements
- Add retry logic for failed requests
- Export to CSV in addition to JSON

---

## ⚠️ Disclaimer

This project is for educational purposes. Always respect website terms of service and API rate limits when scraping or consuming public APIs.
