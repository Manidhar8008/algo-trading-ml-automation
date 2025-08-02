# strategy_backtest.py
import pandas as pd
import ta

stocks = ["RELIANCE", "TCS", "HDFCBANK"]

def apply_strategy(df):
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
    df['SMA20'] = df['Close'].rolling(window=20).mean()
    df['SMA50'] = df['Close'].rolling(window=50).mean()
    df['Buy_Signal'] = ((df['RSI'] < 30) & (df['SMA20'] > df['SMA50'])).astype(int)
    return df

def backtest(stock):
    df = pd.read_csv(f"{stock}.csv")
    df[['Open','High','Low','Close','Volume']] = \
        df[['Open','High','Low','Close','Volume']].apply(pd.to_numeric, errors='coerce')
    df = apply_strategy(df)
    df.to_csv(f"{stock}_strategy.csv", index=False)
    print(f"Backtested: {stock}")

def main():
    for s in stocks:
        backtest(s)

if __name__ == "__main__":
    main()
