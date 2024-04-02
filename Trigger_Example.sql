-- Example of a complex referential integrity using triggers
-- If the current weather at an airport is too severe, it will be temporarily closed for that day until the weather clears. Airports that are already closed for other reasons are not affected. See the trigger in the DML for details.
-- In this example the wind gusts at the airport with location id 1 become too severe for planes to take off for the day.
-- It settles later and the airport reopens. 

-- Status of airport with id 1
SELECT * FROM airport WHERE Location_ID = 1;

-- High winds at airport with location id 1
INSERT INTO weather (weather_date, total_precipitation, wind_gust_max) VALUE (CURDATE(), 2, 90);
INSERT INTO weather_of (SELECT LAST_INSERT_ID(), 1);

SELECT * FROM airport WHERE Location_ID = 1;

-- Reopen airport after wind settles
INSERT INTO weather (weather_date, total_precipitation, wind_gust_max) VALUE (CURDATE(), 2, 22);
INSERT INTO weather_of (SELECT LAST_INSERT_ID(), 1);

SELECT * FROM airport WHERE Location_ID = 1;
