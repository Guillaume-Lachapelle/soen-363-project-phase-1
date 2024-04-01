SELECT *
FROM airport A, has_departure HD
WHERE A.Airport_ID = HD.Airport_ID;