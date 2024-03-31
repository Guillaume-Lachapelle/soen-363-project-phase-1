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

            for row in reader:
                # Extract the necessary fields
                dep_delay = row[3] if row[3] else 0
                iata_code = row[10]
                dep_date_time = row[23]

                # Write insert statements to output file
                output.write(f"INSERT IGNORE INTO Has_Departure (DepDateTime, Delay, Airport_ID) SELECT '{dep_date_time}', {dep_delay}, Airport_ID FROM Airport WHERE IATA_Code = '{iata_code}';\n")

    print("SQL insert statements have been written to DML.sql.")