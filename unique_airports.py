import pandas as pd

def get_unique_airports():
    # Load the data from the CSV file
    df = pd.read_csv('combined_filtered_data.csv')

    # Remove duplicate rows based on the 'name' column
    df_no_duplicates = df.drop_duplicates(subset='name')

    # Write the dataframe without duplicates to a new CSV file
    df_no_duplicates.to_csv('combined_filtered_no_duplicates.csv', index=False)
