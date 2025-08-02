# 🧠 Algo-Trading System with ML & Automation 📈

A complete Python-based prototype that:
- Connects to Yahoo Finance API for stock data 📊
- Implements RSI + Moving Average Crossover Strategy 🔁
- Predicts market movement using a Machine Learning classifier 🤖
- Logs buy signals to Google Sheets automatically 📤

---

## 🔧 Features

- 📥 **Data Ingestion** using `yfinance`
- 📊 **Strategy Logic**: RSI + MA crossover
- 🤖 **ML Model**: Predicts BUY/HOLD based on technical indicators
- 📈 **Backtesting**: Simulates signals on historical data
- 📄 **Google Sheets Logging**: Logs buy signals automatically
- 📂 Modular structure (easy to extend)

---

## 📁 Project Structure

```bash
.
├── data_ingestion.py        # Download stock data
├── strategy_backtest.py     # Implements RSI + MA crossover strategy
├── ml_prediction.py         # ML-based market prediction
├── google_sheet_log.py      # Logs BUY signals to Google Sheets
├── run_all.py               # Runs the full pipeline
├── creds.json               # [Ignored] Google API credentials
├── *.csv                    # Generated stock + strategy data
