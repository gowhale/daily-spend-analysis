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

spending_within_dates = raw_df[raw_df["Within Wanted Range"] == True]

# Remove unwanted transactions

# Create graph for daily spending

# Calculate average daily spend
