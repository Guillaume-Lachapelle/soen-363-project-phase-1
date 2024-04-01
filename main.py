import filter_airports
import combine_filtered_data
import unique_airports
import get_date_intervals
import get_weather
import final_data
import create_dml

print('Running main.py...')
print('Filtering airports...')
filter_airports.filter()
print('Combining filtered data... This step takes a long time, please be patient... :)')
combine_filtered_data.combine_filtered()
print('Getting unique airports...')
unique_airports.get_unique_airports()
print('Getting date intervals...')
get_date_intervals.get_intervals()
# print('Getting weather data... This step takes a long time, please be patient... :)')
# get_weather.get_weather_data()
# print('Creating final data...')
# final_data.get_final_data()
# print('Creating DML...')
# create_dml.create_dml()