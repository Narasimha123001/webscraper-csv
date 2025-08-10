import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scrape_flipkart_redmi(output_path="data/flipkart_redmi.csv"):
    # Setup Selenium in headless mode
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)

    try:
        # Open Flipkart page
        url = "https://www.flipkart.com/search?q=redmi"
        driver.get(url)
        time.sleep(5)  # Allow JavaScript to load

        # Parse HTML
        soup = BeautifulSoup(driver.page_source, "html.parser")

    finally:
        driver.quit()

    # Extract product blocks
    product_blocks = soup.find_all("div", class_="tUxRFH")
    data = []

    for block in product_blocks:
        name_tag = block.find("div", class_="KzDlHZ")
        price_tag = block.find("div", class_="Nx9bqj _4b5DiR")
        discount_tag = block.find("div", class_="UkUFwK")

        product_name = name_tag.get_text(strip=True) if name_tag else "NA"
        current_price = price_tag.get_text(strip=True) if price_tag else "NA"
        discount = discount_tag.get_text(strip=True) if discount_tag else "NA"

        data.append([product_name, current_price, discount])

    # Save to CSV
    df = pd.DataFrame(data, columns=["Product Name", "Current Price", "Discount"])
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"✅ Data saved to {output_path}")

if __name__ == "__main__":
    scrape_flipkart_redmi()
