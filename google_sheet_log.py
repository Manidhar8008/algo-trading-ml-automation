import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# spreadsheet name
GOOGLE_SHEET_NAME = 'Internproject'
# load strategy result (start with RELIANCE, then we automate for all)
result_file = 'RELIANCE_strategy.csv'

# Google auth
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# open google sheet & first tab
sheet = client.open(GOOGLE_SHEET_NAME).sheet1

df = pd.read_csv(result_file)

# log only rows where Buy_Signal = 1
buy_signals = df[df["Buy_Signal"] == 1]

# clear sheet first & insert
sheet.clear()
sheet.update([buy_signals.columns.values.tolist()] + buy_signals.values.tolist())

print("Logged buy signals to Google Sheet!")
