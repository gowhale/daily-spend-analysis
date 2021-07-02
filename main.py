# Program Name: Daily Spend Analysis
# Description:  This script goes through a CSV and then generates daily average spends to help people forecast thier finances.

import pandas as pd
from datetime import datetime

# Variables
date_format = '%d/%m/%Y'
start_date_string = "20/06/2021"
end_date_string = "09/12/2021"

# Load CSV into dataframe
raw_df = pd.read_csv("data.csv")

# Create a dataframe of spends between wanted dates
valid_dates = []

for date in raw_df["Date"]:

    date_obj = datetime.strptime(date, date_format)
    start_date_obj = datetime.strptime(start_date_string, date_format)
    end_date_obj = datetime.strptime(end_date_string, date_format)

    if not (date_obj < start_date_obj) and not (end_date_obj < date_obj):
        valid_dates.append(True)
    else:
        valid_dates.append(False)

raw_df["Within Wanted Range"] = valid_dates

spending_within_dates_df = raw_df[raw_df["Within Wanted Range"] == True]


# Remove unwanted transactions
trimmed_df = spending_within_dates_df
ignore_transation_file = open('unwanted_transactions.txt', 'r')
unwanted_transactions_lines = ignore_transation_file.readlines()

for line in unwanted_transactions_lines:
    stripped_line = (line.strip())
    if stripped_line[:3] == "tx_":
        print(stripped_line)
        trimmed_df = trimmed_df[trimmed_df["Transaction ID"] != stripped_line]
        
trimmed_df.to_csv('transaction_log.csv')

# Create graph for daily spending

# Calculate average daily spend
