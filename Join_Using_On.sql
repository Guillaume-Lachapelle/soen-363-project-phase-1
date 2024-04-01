SELECT *
FROM airport A
JOIN has_departure HD ON A.Airport_ID = HD.Airport_ID;