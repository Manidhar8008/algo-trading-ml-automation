# data_ingestion.py
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]

end_date = datetime.today()
start_date = end_date - timedelta(days=180)

def fetch_data(symbol):
    data = yf.download(symbol, start=start_date, end=end_date, interval='1d')
    data.to_csv(f"{symbol.replace('.NS','')}.csv")
    print(f"Saved: {symbol.replace('.NS','')}.csv")

def main():
    for stock in stocks:
        fetch_data(stock)

if __name__ == "__main__":
    main()
