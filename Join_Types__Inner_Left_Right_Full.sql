-- Insert the values below to get null result
-- INSERT INTO Weather (Weather_Date, Max_Temp, Min_Temp, Mean_Temp, Total_Precipitation, Total_Rain, Total_Snowfall, Precipitation_Hours, Wind_Speed_Max, Wind_Gust_Max)
-- VALUES 
-- ('2024-04-01', 25.0, 15.0, 20.0, 0.0, 0.0, 0.0, 0.0, 10.0, 20.0),
-- ('2024-04-02', 26.0, 16.0, 21.0, 0.1, 0.1, 0.0, 1.0, 12.0, 22.0),
-- ('2024-04-03', 27.0, 17.0, 22.0, 0.2, 0.2, 0.0, 2.0, 14.0, 24.0),
-- ('2024-04-04', 28.0, 18.0, 23.0, 0.3, 0.3, 0.0, 3.0, 16.0, 26.0),
-- ('2024-04-05', 29.0, 19.0, 24.0, 0.4, 0.4, 0.0, 4.0, 18.0, 28.0);
-- INSERT INTO Location (Latitude, Longitude)
-- VALUES 
-- (45.5017, -73.5673),
-- (49.2827, -123.1207),
-- (51.0447, -114.0719),
-- (53.5461, -113.4938),
-- (43.6532, -79.3832);
SELECT L.Location_ID,
    L.Latitude,
    L.Longitude,
    W.Weather_Date,
    W.Max_Temp,
    W.Min_Temp
FROM Location L
    JOIN Weather_Of WO ON L.Location_ID = WO.Location_ID
    JOIN Weather W ON WO.Weather_ID = W.Weather_ID;
-- Locations without a weather record will still be included in the result with NULL in the weather fields.
SELECT L.Location_ID,
    L.Latitude,
    L.Longitude,
    W.Weather_Date,
    W.Max_Temp,
    W.Min_Temp
FROM Location L
    LEFT OUTER JOIN Weather_Of WO ON L.Location_ID = WO.Location_ID
    LEFT OUTER JOIN Weather W ON WO.Weather_ID = W.Weather_ID;
--  Weather records without a corresponding location will still be included in the result with NULL in the location fields.
SELECT L.Location_ID,
    L.Latitude,
    L.Longitude,
    W.Weather_Date,
    W.Max_Temp,
    W.Min_Temp
FROM Location L
    RIGHT OUTER JOIN Weather_Of WO ON L.Location_ID = WO.Location_ID
    RIGHT OUTER JOIN Weather W ON WO.Weather_ID = W.Weather_ID;
--  This query will return all locations and all weather records. If there is no match, the result is NULL on the side that doesn’t have a match.
SELECT L.Location_ID,
    L.Latitude,
    L.Longitude,
    W.Weather_Date,
    W.Max_Temp,
    W.Min_Temp
FROM Location L
    LEFT JOIN Weather_Of WO ON L.Location_ID = WO.Location_ID
    LEFT JOIN Weather W ON WO.Weather_ID = W.Weather_ID
UNION
SELECT L.Location_ID,
    L.Latitude,
    L.Longitude,
    W.Weather_Date,
    W.Max_Temp,
    W.Min_Temp
FROM Location L
    RIGHT JOIN Weather_Of WO ON L.Location_ID = WO.Location_ID
    RIGHT JOIN Weather W ON WO.Weather_ID = W.Weather_ID;