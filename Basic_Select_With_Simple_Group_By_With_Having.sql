SELECT Airport_ID, COUNT(*) AS Departure_With_Over_15h_Delay_Count
FROM has_departure
GROUP BY Airport_ID
HAVING AVG(Delay) > 15;
