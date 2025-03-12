# Ouedkniss Web Scraper

## Overview
This project is a **web scraper** designed to extract email addresses and titles from service listings on **Ouedkniss** using **Selenium and BeautifulSoup**. The extracted data is then saved to a CSV file for further use.

## Technologies Used
- **Python**
- **Selenium** (for browser automation)
- **BeautifulSoup** (for HTML parsing)
- **Requests** (for making GraphQL API requests)
- **Pandas** (for data storage & manipulation)

## Features
- **Automated navigation** through service listings
- **Data extraction** including titles and emails from each listing
- **GraphQL API interaction** to fetch listing details
- **CSV file export** for structured data storage

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/saidililia/Web-Scraping.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Download and place the **Chrome WebDriver** in your system path. 
   - [ChromeDriver Download](https://chromedriver.chromium.org/downloads)

## Usage
Run the script with:
```sh
python scraper.py
```

## How It Works
1. The script sends GraphQL requests to fetch **service listing details**.
2. It extracts **titles and listing URLs**.
3. Selenium is used to **visit each listing page** and extract the **email address**.
4. The extracted data is stored in a **CSV file** (`Ouedkniss/Email.csv`).

## Example Output
```
Extracted Data:
---------------------
Title: Event Management Services
Email: contact@example.com
...
```

## Future Improvements
- Implement **proxy rotation** and **headless mode** for better performance.
- Store data in a **database** (MySQL, MongoDB, etc.).
- Add **error handling** and **retry mechanisms**.

## Legal Disclaimer
This project is intended for educational purposes only. Ensure compliance with **Ouedkniss's terms of service** before scraping.

## Contact
For inquiries, reach out via Email: saidililia555@gmail.com or visit my GitHub profile: [GitHub Profile Link].
