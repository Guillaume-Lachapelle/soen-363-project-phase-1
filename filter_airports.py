import csv

def filter():
    # Open the input and output files
    with open('airport-codes.csv', 'r', encoding='utf-8') as csvinput, open('filtered_airports.csv', 'w', newline='', encoding='utf-8') as csvoutput:
        # Create the CSV reader and writer
        reader = csv.reader(csvinput)
        writer = csv.writer(csvoutput)

        # Write the header to the output file
        header = next(reader)
        writer.writerow(header)

        # Get the index of the 'continent' and 'iso_country' columns
        continent_index = header.index('continent')
        country_index = header.index('iso_country')

        # Iterate over the rows
        for row in reader:
            # Check if the 'continent' is 'NA' and 'iso_country' is 'US'
            if row[continent_index] == 'NA' and row[country_index] == 'US':
                # Write the row to the output file
                writer.writerow(row)
