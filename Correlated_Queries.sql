SELECT A.Airport_Name,
    AVG(D.Delay) AS Average_Delay
FROM Airport A
    INNER JOIN Has_Departure D ON A.Airport_ID = D.Airport_ID
GROUP BY A.Airport_ID
HAVING Average_Delay > (
        SELECT AVG(Delay)
        FROM Has_Departure
    )
ORDER BY Average_Delay;
SELECT AVG(Delay) AS Average_Delay
FROM Has_Departure;
SELECT L.Location_ID,
    MAX(W.Max_Temp) AS Max_Temperature
FROM Location L
    INNER JOIN Weather_Of WO ON L.Location_ID = WO.Location_ID
    INNER JOIN Weather W ON WO.Weather_ID = W.Weather_ID
GROUP BY L.Location_ID
HAVING Max_Temperature > (
        SELECT AVG(Max_Temp)
        FROM Weather
    )
ORDER BY Max_Temperature;
SELECT AVG(Max_Temp) AS Average_Max_Temperature
FROM Weather;