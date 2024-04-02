-- An example of a view that has a hard-coded criteria, by which the content of the view
-- may change upon changing the hard-coded value (see L09 slide 24).

CREATE VIEW LargeAirports AS
(SELECT * FROM Airport WHERE Airport_Type = 'Large');