import pandas as pd
from datetime import datetime

def combine_filtered():
    # Load the data from the CSV files
    combine_df = pd.read_csv('combine_files.csv', dtype={19: str, 25: str})
    filtered_airports_df = pd.read_csv('filtered_airports.csv')

    # Merge the dataframes on the 'Origin' and 'iata_code' columns
    merged_df = pd.merge(combine_df, filtered_airports_df, left_on='Origin', right_on='iata_code')

    # Filter the columns
    filtered_columns_df = merged_df[['Year', 'Month', 'DayofMonth', 'DepTime', 'DepDelay', 'type', 'name', 'continent', 'iso_country', 'iso_region', 'municipality', 'iata_code', 'coordinates']].copy()

    # Create the 'DepartureDate' column
    filtered_columns_df['date'] = pd.to_datetime(filtered_columns_df[['Year', 'Month', 'DayofMonth']].astype(str).agg('-'.join, axis=1))
    filtered_columns_df.rename(columns={'DepartureDate': 'date'}, inplace=True)

    # Split the 'coordinates' column into 'latitude' and 'longitude'
    filtered_columns_df[['latitude', 'longitude']] = filtered_columns_df['coordinates'].str.split(', ', expand=True)
    
    # For the 'DepTime' column, convert the float values to HH:MM format
    filtered_columns_df['DepTime'] = filtered_columns_df['DepTime'].apply(lambda x: '{:04}'.format(int(x)) if pd.notnull(x) else '0000')
    filtered_columns_df['DepTime'] = filtered_columns_df['DepTime'].apply(lambda x: f"{x.zfill(4)[:2]}:{x.zfill(4)[2:]}")
    
    # Write the final dataframe to a new CSV file
    filtered_columns_df.to_csv('combined_filtered_data.csv', index=False)
