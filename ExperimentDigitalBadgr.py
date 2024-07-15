import pandas as pd

# Download tracker Google Sheets as csv and input its local filepath
filepath = input("path to csv file: ")

# Read into dataframes 
og_df = pd.read_csv(input)

# Input which week this is for
week = input("Which week is this tracker for? (eg. 1, 2, etc.)")

# Make new filename
name = "TED Week" + week + " badge.csv"

# Filter rows where the 'Weekly Completion' column has 'Yes'
filtered_df = og_df[og_df['Weekly Completion'] == 'Yes']

# Save the filtered DataFrame to a new CSV file without the index
filtered_df.to_csv(name, index=False)