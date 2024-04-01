SELECT Airport_Type, COUNT(*) as Total_Airports
FROM airport
GROUP BY Airport_Type;
