
---

# 📱 Flipkart Redmi Phone Web Scraper

## 📌 Overview

This Python  project scrapes **product details** — such as **name, price, and discount** — for **Redmi smartphones** from [Flipkart](https://www.flipkart.com/) using **Selenium** and **BeautifulSoup**, then saves them into a **CSV file** for further analysis.

> ⚠ **Disclaimer:** This script is for **educational purposes only**. Web scraping Flipkart may violate its Terms of Use. Ensure you have permission before running it on their live website.

---

## 📂 Project Structure

```
flipkart_scraper/
├── data/                     # Output CSV files
│   └── flipkart_redmi.csv    # Scraped data
├── tests/                    # Unit tests
│   └── test_scraper.py
├── .github/workflows/        # CI pipeline
│   └── python-app.yml
├── config.py                 # Configuration (URL, output file path)
├── scraper.py                # Main scraper script
├── requirements.txt          # Project dependencies
├── README.md                 # Documentation
└── .gitignore                # Ignored files
```

---

## ⚙ Dependencies

* **Python** ≥ 3.8
* **Google Chrome** browser
* **ChromeDriver** (matching your Chrome version)
* **Python Libraries**:

  * `selenium`
  * `beautifulsoup4`
  * `pandas`

📄 Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/flipkart-scraper.git
cd flipkart-scraper
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
# Activate the environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install ChromeDriver

* Check your Chrome browser version.
* Download the matching **ChromeDriver** from: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
* Add ChromeDriver to your **system PATH**.

---

## 🚀 Usage

Run the scraper:

```bash
python scraper.py
```

The output will be saved at:

```
data/flipkart_redmi.csv
```

---

## 🛠 How It Works

1. Opens Flipkart’s search results for **Redmi phones** in headless Chrome.
2. Waits for JavaScript content to fully load.
3. Parses HTML using **BeautifulSoup**.
4. Extracts:

   * Product Name
   * Current Price
   * Discount
5. Saves the results into a CSV file.

---

## 📜 Example Output

| Product Name       | Current Price | Discount |
| ------------------ | ------------- | -------- |
| Redmi Note 12      | ₹14,999       | 10% off  |
| Redmi 12C          | ₹8,499        | 15% off  |
| Redmi Note 11 Pro+ | ₹20,999       | 12% off  |

---

## 🧪 Running Tests

Run unit tests to ensure scraper works correctly:

```bash
pytest tests/
```

---

## 🔧 Configuration

Edit `config.py` to change:

```python
FLIPKART_URL = "https://www.flipkart.com/search?q=redmi"
OUTPUT_FILE = "data/flipkart_redmi.csv"
```

---

## 📄 License 

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it with proper attribution.
