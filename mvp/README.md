# Algo Trading ML Automation - MVP

This project is an end-to-end scaffold to build a daily pre-market alert system that ranks a universe of stocks by predicted short-term returns and produces BUY/SELL alerts. The goal is to teach each step: data collection, feature engineering, model training, backtesting, alert generation, and deployment.

Structure (mvp):
- configs/config.yaml  # configuration for runs
- data/                # data is written here (raw/processed)
- models/              # trained model artifacts
- src/                 # source code
  - data/ downloader.py
  - features/ engineer.py
  - models/ train.py
  - backtest/ backtester.py
  - alerts/ generate_alerts.py
- scripts/ run_daily.sh
- notebooks/01_mvp_walkthrough.md

Quick start (local, MVP):
1. Create a Python venv and install requirements: pip install -r requirements.txt
2. Edit configs/config.yaml if needed (dates, universe)
3. Run scripts/run_daily.sh to download data, train a baseline model, run a backtest, and produce today's alert CSV in outputs/alerts.csv

