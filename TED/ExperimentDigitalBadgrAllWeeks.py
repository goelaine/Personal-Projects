import pandas as pd

# Download summary tracker Google Sheets as csv and input its local filepath
filepath = input("path to csv file: \n")

# Read into dataframes 
og_df = pd.read_csv(filepath, header=2)

# Input your name
fam = input("Your first name?\n")

for week in range(1,7):
    # Make new filename
    name = "TED Week" + str(week) + " badge.csv"
    print(f"Name: {name}")

    # Input corresponding date 
    prompt = "What is the issue date for week " + str(week) + "? in MM-DD-YY format\n"
    date = input(prompt)

    # strip extraneous spaces out of column headers
    og_df.columns = og_df.columns.str.rstrip()

    # Filter rows where the specified week is 'completed' and the student belongs to your family
    # filter_df = og_df[(og_df['Weekly Completion'] == 'Yes') & ((og_df['Family']== (fam + ' 1')) | (og_df['Family']== (fam + ' 2')))]
    filter_df = og_df[(og_df.iloc[:,10+int(week)] == 'Complete') & ((og_df['Family']== (fam + ' 1')) | (og_df['Family']== (fam + ' 2')))]

    # Only keep columns with necessary information
    filter_df = filter_df[['Full Name', 'Email']]

    # Rename email to identifier
    filter_df.rename(columns={'Email': 'Identifier'}, inplace=True)

    # insert the issue date into csv
    filter_df['Issue Date'] = date

    # Save the filtered DataFrame to a new CSV file without the index
    filter_df.to_csv(name, index=False)

print("done")