# Program Name: Daily Spend Analysis
# Description:  This script goes through a CSV and then generates daily average spends to help people forecast thier finances.

import pandas as pd
from datetime import datetime
import plotly.express as px

# Variables
date_format = '%d/%m/%Y'
start_date_string = "08/06/2021"
end_date_string = "05/07/2021"

# Load CSV into dataframe
raw_df = pd.read_csv("data.csv")

# Create a dataframe of spends between wanted dates
valid_dates = []
start_date_obj = datetime.strptime(start_date_string, date_format)
end_date_obj = datetime.strptime(end_date_string, date_format)

for date in raw_df["Date"]:

    date_obj = datetime.strptime(date, date_format)

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

trimmed_df.to_csv('trimmed_dataset.csv')

# Create a daily expenses dataframe

expenses = trimmed_df[trimmed_df["Amount"] < 0]
expenses["Amount"] = expenses["Amount"].abs()
income = trimmed_df[trimmed_df["Amount"] > 0]

list_of_date_range = pd.date_range(start=start_date_obj, end=end_date_obj)
list_of_date_range = list_of_date_range.strftime(date_format)

daily_dates = []
daily_sums = []

for date in list_of_date_range:
    daily_dates.append(date)
    date_sum = expenses[expenses["Date"] == date]["Amount"].sum()
    daily_sums.append(date_sum)
    print((date, date_sum))

daily_expenses_df = pd.DataFrame(
    {'Date': daily_dates,
     'Amount': daily_sums,
     })

daily_expenses_df.to_csv("daily_expeneses.csv")

# Create graph for daily spending

print("\n\nCreating graph...")
fig = px.scatter(daily_expenses_df, x="Date", y="Amount", color="Amount",
                 color_continuous_scale=["green", "orange", "red", ],)
fig.update_traces(marker=dict(size=12))
fig.update_yaxes(range=[0, 200])
fig.update_layout(
    title="Daily Spends",
    xaxis_title="Date",
    yaxis_title="Amount (GDP)",
    font=dict(
        family="Arial",
        size=25,
        color="#7f7f7f"
    )
)

print("Graph created.")
fig.show()
print("Graph saved.")

# Calculate average daily spend
