import pandas as pd

def get_intervals():
    # Load the data from the CSV file
    df = pd.read_csv('combined_filtered_data.csv')

    # Convert 'date' to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Group by 'name' and calculate min and max dates
    date_intervals_df = df.groupby('name').agg({'date': ['min', 'max'], 'latitude': 'first', 'longitude': 'first'}).reset_index()

    # Flatten the MultiIndex columns
    date_intervals_df.columns = ['_'.join(col).strip('_') for col in date_intervals_df.columns.values]

    # Rename the columns
    # date_intervals_df.rename(columns={'date_min': 'date_min', 'date_max': 'date_max'}, inplace=True)

    # Write the dataframe to a new CSV file
    date_intervals_df.to_csv('date_intervals.csv', index=False)
