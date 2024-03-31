-- CREATE DATABASE soen363_project_phase1;
USE soen363_project_phase1;

CREATE TABLE Location (
    Location_ID INT PRIMARY KEY AUTO_INCREMENT,
    Latitude DECIMAL(15,10) CHECK (Latitude >= -90 AND Latitude <= 90),
    Longitude DECIMAL(15, 10) CHECK (Longitude >= -180 AND Longitude <= 180)
);

CREATE TABLE Airport (
    Airport_ID INT PRIMARY KEY AUTO_INCREMENT,
    IATA_Code VARCHAR(3),
    Airport_Type ENUM('Small', 'Medium', 'Large'),
    Airport_Name VARCHAR(100),
    Municipality VARCHAR(100),
    Airport_Status ENUM('Open', 'Closed', 'Temporarily Closed'),
    Location_ID INT,
    FOREIGN KEY (Location_ID) REFERENCES Location(Location_ID)
);

CREATE TABLE Has_Departure (
    DepDateTime DATETIME,
    Delay FLOAT,
    Airport_ID INT,
    FOREIGN KEY (Airport_ID) REFERENCES Airport(Airport_ID) ON DELETE CASCADE,
    PRIMARY KEY (DepDateTime, Airport_ID)
);

CREATE TABLE Weather (
    Weather_ID INT PRIMARY KEY AUTO_INCREMENT,
    Weather_Date DATETIME,
    Max_Temp FLOAT,
    Min_Temp FLOAT,
    Mean_Temp FLOAT,
    Total_Precipitation FLOAT,
    Total_Rain FLOAT,
    Total_Snowfall FLOAT,
    Precipitation_Hours FLOAT,
    Wind_Speed_Max FLOAT,
    Wind_Gust_Max FLOAT
);

CREATE TABLE Weather_Of (
    Weather_ID INT,
    Location_ID INT,
    FOREIGN KEY (Weather_ID) REFERENCES Weather(Weather_ID),
    FOREIGN KEY (Location_ID) REFERENCES Location(Location_ID),
    PRIMARY KEY (Weather_ID, Location_ID)
);

DELIMITER //
CREATE TRIGGER update_airport_status
AFTER INSERT ON Weather_Of
FOR EACH ROW
BEGIN
    DECLARE precip FLOAT;

    SELECT Total_Precipitation INTO precip FROM Weather WHERE Weather_ID = NEW.Weather_ID;

    IF precip > 10 THEN
        UPDATE Airport
        SET Airport_Status = 'Temporarily Closed'
        WHERE Location_ID = NEW.Location_ID;
    END IF;
END;//
DELIMITER ;