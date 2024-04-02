import openmeteo_requests
import requests
from retry_requests import retry
import pandas as pd
import time

def get_weather_data(startIndex=None):
    if startIndex is None:
        startIndex = 0
    else:
        startIndex = int(startIndex)

    # Load the data from the CSV file
    date_intervals_df = pd.read_csv('date_intervals.csv', skiprows=range(1, startIndex + 1))

    # Setup the Open-Meteo API client with retry on error
    retry_session = retry(requests.Session(), retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # URL for the Open-Meteo API
    url = "https://archive-api.open-meteo.com/v1/archive"

    # Create an empty DataFrame to store all the data
    all_data = pd.DataFrame()

    rowIndex = startIndex
    # Iterate over all the rows in the dataframe
    for i, row in date_intervals_df.iterrows():
        # Parameters for the Open-Meteo API request
        params = {
            "latitude": row['latitude_first'],
            "longitude": row['longitude_first'],
            "start_date": row['date_min'],
            "end_date": row['date_max'],
            "daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "precipitation_sum", "rain_sum", "snowfall_sum", "precipitation_hours", "wind_speed_10m_max", "wind_gusts_10m_max"]
        }

        crashed = False
        # Make the Open-Meteo API request
        while True:
            try:
                print('Requesting weather data...' + row['name'])
                responses = openmeteo.weather_api(url, params=params)
                break
            except Exception as e:
                if 'Hourly API request limit exceeded' in e.args[0]['reason'] or 'Daily API request limit exceeded' in e.args[0]['reason']:
                    print(e.args[0]['reason'])
                    print("stopped at row index: " + str(rowIndex))
                    crashed = True
                    break

                print('Limit exceeded, waiting for 60 seconds... Do not interrupt the program!')
                time.sleep(60)  # wait for 60 seconds before making the next request

        rowIndex += 1
        if crashed:
            break

        # Process the response
        response = responses[0]

        # Process daily data
        daily = response.Daily()
        daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
        daily_temperature_2m_mean = daily.Variables(2).ValuesAsNumpy()
        daily_precipitation_sum = daily.Variables(3).ValuesAsNumpy()
        daily_rain_sum = daily.Variables(4).ValuesAsNumpy()
        daily_snowfall_sum = daily.Variables(5).ValuesAsNumpy()
        daily_precipitation_hours = daily.Variables(6).ValuesAsNumpy()
        daily_wind_speed_10m_max = daily.Variables(7).ValuesAsNumpy()
        daily_wind_gusts_10m_max = daily.Variables(8).ValuesAsNumpy()

        # Create a dataframe from the daily data
        daily_data = {
            "name": row['name'],
            "latitude": row['latitude_first'],
            "longitude": row['longitude_first'],
            "date": pd.date_range(
                start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
                end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
                freq = pd.Timedelta(seconds = daily.Interval()),
                inclusive = "left"
            ).normalize(),  # normalize() removes the time component
            "temperature_2m_max": daily_temperature_2m_max,
            "temperature_2m_min": daily_temperature_2m_min,
            "temperature_2m_mean": daily_temperature_2m_mean,
            "precipitation_sum": daily_precipitation_sum,
            "rain_sum": daily_rain_sum,
            "snowfall_sum": daily_snowfall_sum,
            "precipitation_hours": daily_precipitation_hours,
            "wind_speed_10m_max": daily_wind_speed_10m_max,
            "wind_gusts_10m_max": daily_wind_gusts_10m_max
        }

        daily_dataframe = pd.DataFrame(data = daily_data)

        # Append the data to the all_data DataFrame
        all_data = pd.concat([all_data, daily_dataframe], ignore_index=True)

    if startIndex == 0:
        # Write the all_data DataFrame to a CSV file
        all_data.to_csv('weather_per_location.csv', index=False)
    else:
        # Append the data to an existing CSV file
        all_data.to_csv('weather_per_location.csv', mode='a', header=False, index=False)

if __name__ == '__main__':
    # Get user input
    user_input = input("Index to resume at (0 if starting from beginning): ")

    print('Getting weather data... This step takes a long time, please be patient... :)')
    get_weather_data(user_input)