-- Division
-- Find all airports that had depatures on 2016-01-01, 2016-01-02, 2016-01-03 and 2016-12-25
-- has_departure / desired departure dates
-- A / S

-- Setup
CREATE TABLE desired_dates (
	DesiredDate DATE PRIMARY KEY
);
INSERT INTO desired_dates VALUES ('2016-01-01'), ('2016-01-02'), ('2016-01-03'), ('2016-12-25');

-- a) a regular nested query using NOT IN
SELECT DISTINCT Airport_ID FROM has_departure 
WHERE Airport_ID NOT IN 
	(SELECT Airport_ID FROM (
		(SELECT Airport_ID , DesiredDate FROM (SELECT DesiredDate FROM desired_dates ) AS DesiredDates CROSS JOIN 
		(SELECT DISTINCT Airport_ID FROM has_departure) AS Airports)
		EXCEPT
		(SELECT DISTINCT Airport_ID, CAST(DepDateTime AS DATE) FROM has_departure) 
        ) AS AirportsWithoutDesiredDates
	);
    

-- b) a correlated nested query using NOT EXISTS and EXCEPT
SELECT DISTINCT Airport_ID FROM has_departure AS airports
WHERE NOT EXISTS (
	(SELECT DesiredDate FROM desired_dates)
	EXCEPT
	(SELECT CAST(deps.DepDateTime AS DATE) FROM  has_departure AS deps WHERE deps.Airport_ID = airports.Airport_ID) 
);

-- Clean up
DROP TABLE desired_dates;