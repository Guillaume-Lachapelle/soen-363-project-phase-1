-- Overlap Constraint: To demonstrate an overlap where airports have both departures and are listed as ‘Open’
SELECT DISTINCT a.Airport_ID
FROM Airport a
JOIN Has_Departure d ON a.Airport_ID = d.Airport_ID
WHERE a.Airport_Status = 'Open';


-- Covering Constraint: To ensure that all airports with departures also have weather data
SELECT DISTINCT a.Airport_ID, a.Airport_Name
FROM Airport a
JOIN Weather_Of w ON a.Location_ID = w.Location_ID
JOIN Has_Departure d ON a.Airport_ID = d.Airport_ID;