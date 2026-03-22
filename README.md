# Internshala Python Internship Scraper

## 📌 Overview

This project is a Python-based web scraper that extracts internship listings from Internshala. It collects data from multiple pages and organizes it into a structured format for analysis.

## ⚙️ Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas

## 🚀 Features

* Scrapes multiple pages of internship listings
* Extracts key details such as:

  * Job Role
  * Company Name
  * Location
  * Stipend
  * Required Skills
* Stores data in a Pandas DataFrame
* Option to export data to CSV

## 📂 Project Structure

```
scrap-internshala/
│── internshala.py
│── README.md
```

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Abhilash-Alle/scrap-project-internshala.git
cd scrap-internshala
```

2. Install dependencies:

```bash
pip install requests beautifulsoup4 pandas lxml
```

3. Run the script:

```bash
python internshala.py
```

## 📊 Output

The script prints the scraped data in a DataFrame format and can optionally save it as a CSV file.

## ⚠️ Disclaimer

* This project is for educational purposes only.
* The scraper depends on Internshala’s website structure. If the HTML changes, the code may need updates.

## ✍️ Author

Abhilash Alle

