import os
import pandas as pd
import ta
from datetime import datetime, timedelta
import yfinance as yf
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# STEP 1: Download data
stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
end_date = datetime.today()
start_date = end_date - timedelta(days=180)

for symbol in stocks:
    data = yf.download(symbol, start=start_date, end=end_date, interval='1d')
    data.to_csv(f"{symbol.replace('.NS','')}.csv")
    print(f"Downloaded: {symbol}")

# STEP 2: Apply strategy
def apply_strategy(df):
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
    df['SMA20'] = df['Close'].rolling(window=20).mean()
    df['SMA50'] = df['Close'].rolling(window=50).mean()
    df['Buy_Signal'] = ((df['RSI'] < 30) & (df['SMA20'] > df['SMA50'])).astype(int)
    return df

for stock in ["RELIANCE", "TCS", "HDFCBANK"]:
    df = pd.read_csv(f"{stock}.csv")
    df[['Open','High','Low','Close','Volume']] = df[['Open','High','Low','Close','Volume']].apply(pd.to_numeric, errors='coerce')
    df = apply_strategy(df)
    df.to_csv(f"{stock}_strategy.csv", index=False)
    print(f"Backtested: {stock}")

# STEP 3: ML Prediction
df = pd.read_csv("RELIANCE.csv")
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
df['MACD'] = ta.trend.MACD(df['Close']).macd()
df['SMA50'] = df['Close'].rolling(window=50).mean()
df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
df.dropna(inplace=True)

X = df[['RSI', 'MACD', 'SMA50', 'Volume']]
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"ML Prediction Accuracy (RELIANCE): {acc * 100:.2f}%")

# STEP 4: Log to Google Sheet
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds_path = os.path.join(os.path.dirname(__file__), "creds.json")
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)

client = gspread.authorize(creds)
sheet = client.open("Internproject").sheet1

df = pd.read_csv("RELIANCE_strategy.csv")
buy_signals = df[df["Buy_Signal"] == 1]
sheet.clear()
sheet.update([buy_signals.columns.values.tolist()] + buy_signals.values.tolist())
print("📊 Buy signals logged to Google Sheet!")
