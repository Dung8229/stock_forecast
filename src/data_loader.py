import yfinance as yf
import pandas as pd

def fetch_gold_data(start="2010-01-01", end="2024-01-01"):
    gold = yf.download('GC=F', start=start, end=end)
    gold.to_csv('data/raw/gold_prices.csv')
    return gold

if __name__ == "__main__":
    gold = fetch_gold_data()
    print("Dữ liệu đã tải xong:", gold.head())