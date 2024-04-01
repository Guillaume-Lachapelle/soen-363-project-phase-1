import csv

def create_dml():
    # Open the CSV file and output file
    with open('combined_filtered_no_duplicates.csv', 'r') as file, open('DML.sql', 'w') as output:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            # Extract the necessary fields
            airport_type = row[5]
            airport_name = row[6].replace("'", "").replace("-", " ")  # Remove ' and replace - with space
            municipality = row[10].replace("'", "").replace("-", " ")  # Remove ' and replace - with space
            iata_code = row[11]
            latitude = row[14]
            longitude = row[15]

            # Map the airport_type to the correct ENUM value and exclude unwanted types
            if airport_type == 'small_airport':
                airport_type = 'Small'
            elif airport_type == 'medium_airport':
                airport_type = 'Medium'
            elif airport_type == 'large_airport':
                airport_type = 'Large'
            else:
                continue  # Skip this row if the airport_type is not one of the above
            
            airport_status = 'Open'
            
            # Write insert statements to output file
            output.write(f"INSERT INTO Location (Latitude, Longitude) VALUES ({latitude}, {longitude});\n")
            output.write(f"INSERT INTO Airport (IATA_Code, Airport_Type, Airport_Name, Municipality, Airport_Status, Location_ID) VALUES ('{iata_code}', '{airport_type}', '{airport_name}', '{municipality}', '{airport_status}', LAST_INSERT_ID());\n")

        # Open the final_data.csv file
        with open('final_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for i, row in enumerate(reader):
                
                # Extract the necessary fields
                dep_delay = row[3] if row[3] else 0
                iata_code = row[10]
                dep_date_time = row[23]
                temperature_2m_max = row[14]
                temperature_2m_min = row[15]
                temperature_2m_mean = row[16]
                precipitation_sum = row[17]
                rain_sum = row[18]
                snowfall_sum = row[19]
                precipitation_hours = row[20]
                wind_speed_10m_max = row[21]
                wind_gusts_10m_max = row[22]

                # Write insert statements to output file
                output.write(f"INSERT IGNORE INTO Has_Departure (DepDateTime, Delay, Airport_ID) SELECT '{dep_date_time}', {dep_delay}, Airport_ID FROM Airport WHERE IATA_Code = '{iata_code}';\n")
                
                # Write insert statements for Weather and Weather_Of tables
                output.write(f"INSERT INTO Weather (Weather_Date, Max_Temp, Min_Temp, Mean_Temp, Total_Precipitation, Total_Rain, Total_Snowfall, Precipitation_Hours, Wind_Speed_Max, Wind_Gust_Max) VALUES ('{dep_date_time}', {temperature_2m_max}, {temperature_2m_min}, {temperature_2m_mean}, {precipitation_sum}, {rain_sum}, {snowfall_sum}, {precipitation_hours}, {wind_speed_10m_max}, {wind_gusts_10m_max});\n")
                output.write(f"INSERT INTO Weather_Of (Weather_ID, Location_ID) SELECT LAST_INSERT_ID(), Location_ID FROM Airport WHERE IATA_Code = '{iata_code}';\n")

    print("SQL insert statements have been written to DML.sql.")