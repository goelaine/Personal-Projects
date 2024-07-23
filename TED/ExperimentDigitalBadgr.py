import pandas as pd

# Download summary tracker Google Sheets as csv and input its local filepath
filepath = input("path to csv file: \n")

# Read into dataframes 
og_df = pd.read_csv(filepath, header=2)

# Input which week this is for
week = input("Which week is this tracker for? (eg. 1, 2, etc.)\n")

# Input today's date
date = input("What is today's date? in MM-DD-YY format\n")

# Input your name
fam = input("Your first name?\n")

# Make new filename
name = "TED Week" + week + " badge.csv"
print(f"Name: {name}")

# strip extraneous spaces out of column headers
og_df.columns = og_df.columns.str.rstrip()

# Filter rows where the specified week is 'completed' and the student belongs to your family
filter_df = og_df[(og_df['Week '+week] == 'Complete') & ((og_df['Family']== (fam + ' 1')) | (og_df['Family']== (fam + ' 2')))]

# Only keep columns with necessary information
filter_df = filter_df[['Full Name', 'Email']]

# Rename email to identifier
filter_df.rename(columns={'Email': 'Identifier'}, inplace=True)

# insert the issue date into csv
filter_df['Issue Date'] = date

# Save the filtered DataFrame to a new CSV file without the index
filter_df.to_csv(name, index=False)

print("done")