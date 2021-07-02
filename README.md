# daily-spend-analysis

The aim of this script is to process a CSV of transactions, and output a graph and a value for the CSV's daily spending average.

## Source Data

This script takes in a CSV called "data.csv" and it has the following headings:

    Transaction ID,Date,Time,Type,Name,Emoji,Category,Amount,Currency,Local amount,Local currency,Notes and #tags,Address,Receipt,Description,Category split,Money Out,Money In
    
## Process

The following steps are taken to process the data:

1. Date variables are entered to specify wanted date range
2. CSV is loaded into dataframe
3. dataframe is trimmed to be between wanted dates
4. unwanted transactions taken from "unwanted_transactions.txt" are removed from the dataframe
5. A daily expenses is created and saved to .csv
6. Daily expenses dataframe is visualised on a graph
7. Avarage daily spend is printed to terminal

## Example Graph Output 

This script generates an interactive graph which looks like this:

<img width="1783" alt="example_graph" src="https://user-images.githubusercontent.com/32711718/124261402-a6e2fa80-db28-11eb-85e4-7c936c472ade.png">

## Example Terminal Output

    The average daily spend between 25/06/2021 and 01/07/2021 is £23.09
    
## Requirements

This script was last executed using Pyhton 3.8.5 and requires pandas and plotly modules. Use the following command to install needed modules:

    pip3 install -r requirements.txt
