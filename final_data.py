import pandas as pd

def get_final_data():
    # Load the data from the CSV files
    combined_filtered_data_df = pd.read_csv('combined_filtered_data.csv', encoding='utf-8')
    weather_per_location_df = pd.read_csv('weather_per_location.csv', encoding='utf-8')

    # Convert 'date' to datetime and remove the time component in both dataframes
    combined_filtered_data_df['date'] = pd.to_datetime(combined_filtered_data_df['date']).dt.date
    weather_per_location_df['date'] = pd.to_datetime(weather_per_location_df['date']).dt.date

    # Merge the dataframes on the 'name', 'latitude', 'longitude', and 'date' columns
    merged_df = pd.merge(combined_filtered_data_df, weather_per_location_df, on=['name', 'latitude', 'longitude', 'date'])
    
    # Combine 'date' and 'DepTime' columns into a single 'DepartureDateTime' column
    merged_df['DepartureDateTime'] = pd.to_datetime(merged_df['date'].astype(str) + ' ' + merged_df['DepTime'])
    # Drop the 'date' and 'DepTime' columns
    merged_df.drop(columns=['date', 'DepTime'], inplace=True)

    # Write the first 1500000 rows of the merged dataframe to a new CSV file
    merged_df.head(1500000).to_csv('final_data.csv', index=False, encoding='utf-8')