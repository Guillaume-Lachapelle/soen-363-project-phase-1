-- NOTE: when opening this file in mysql workbench it may appear like there are errors but this is due to a bug in mysql workbench. The queries still run fine when the execute button is clicked on mysql version 8.0.36
-- One example per set operations: intersect, union, and difference vs. their equivalences without using set operations

-- Get all small airports that have departures on on '2016-01-01'
-- Intersect set operation
(SELECT a.Airport_ID, a.IATA_Code, a.Airport_Name FROM airport a
WHERE a.Airport_Type = 'Small')
INTERSECT
(SELECT  a.Airport_ID, a.IATA_Code, a.Airport_Name FROM airport a
JOIN has_departure d ON a.Airport_ID = d.Airport_ID
WHERE CAST(d.DepDateTime AS DATE) = '2016-01-01');
-- Equivalence without set operation
SELECT DISTINCT a.Airport_ID, a.IATA_Code, a.Airport_Name FROM airport a
JOIN has_departure d ON a.Airport_ID = d.Airport_ID
WHERE a.Airport_Type = 'Small' AND CAST(d.DepDateTime AS DATE) = '2016-01-01';

-- Get all large airports or airports that have departures on on '2016-01-01'
-- Union set operation
(SELECT a.Airport_ID, a.IATA_Code, a.Airport_Name FROM airport a
WHERE a.Airport_Type = 'Large')
UNION
(SELECT  a.Airport_ID, a.IATA_Code, a.Airport_Name FROM airport a
JOIN has_departure d ON a.Airport_ID = d.Airport_ID
WHERE CAST(d.DepDateTime AS DATE) = '2016-01-01');
-- Equivalence without set operation
SELECT DISTINCT a.Airport_ID, a.IATA_Code, a.Airport_Name FROM airport a
JOIN has_departure d ON a.Airport_ID = d.Airport_ID
WHERE a.Airport_Type = 'Small' OR CAST(d.DepDateTime AS DATE) = '2016-01-01';

-- Get all airports that have no departures
-- Difference set operation
(SELECT a.Airport_ID, a.IATA_Code, a.Airport_Name FROM Airport a)
EXCEPT
(SELECT a.Airport_ID, a.IATA_Code, a.Airport_Name FROM Airport a
JOIN has_departure d ON a.Airport_ID = d.Airport_ID);
-- Equivalence without set operation
SELECT a.Airport_ID, a.IATA_Code, a.Airport_Name FROM Airport a
WHERE a.Airport_ID NOT IN (SELECT Airport_ID FROM has_departure);