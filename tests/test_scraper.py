import os
import pandas as pd
import subprocess

# Path to the CSV output file
CSV_PATH = "data/flipkart_redmi.csv"

def setup_module(module):
    """
    Runs the scraper before tests if the CSV file doesn't exist.
    """
    if not os.path.exists(CSV_PATH):
        print(f"⚠ CSV not found, running scraper to generate {CSV_PATH}...")
        subprocess.run(["python", "scraper.py"], check=True)

def test_csv_exists():
    """
    Test that the CSV file exists after running the scraper.
    """
    assert os.path.exists(CSV_PATH), "❌ CSV file not found after running scraper."

def test_csv_content():
    """
    Test that the CSV file has expected columns and no missing values.
    """
    df = pd.read_csv(CSV_PATH)
    
    assert not df.empty, "❌ CSV file is empty."
    assert "Product Name" in df.columns, "Missing 'Product Name' column."
    assert "Current Price" in df.columns, "Missing 'Current Price' column."
    assert df["Product Name"].notna().all(), "❌ Some product names are missing."
    assert df["Current Price"].notna().all(), "❌ Some product prices are missing."
