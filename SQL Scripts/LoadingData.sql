LOAD DATA INFILE 'F:/University stage/Submission/CSV Files/PlayerTableFinalL.csv'
INTO TABLE Player
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(playerName, `Position`, Nationality, dateOfBirth, @vHeight, @vWeight)
SET
Weight = NULLIF(@vWeight,''),
Height = NULLIF(@vHeight,'');

LOAD DATA INFILE 'F:/University stage/Submission/CSV Files/StadiumTableFinal.csv'
INTO TABLE Stadium
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(stadiumName, @capacity, @vrecordLeagueAttendance, @buildingDate, lengthBitchSize ,widthBitchSize,addressStreet,addressCity,addressPostalCode)
set 
buildingDate = NULLIF(@buildingDate,''),
recordLeagueAttendance=NULLIF(@vrecordLeagueAttendance,''),
capacity = NULLIF(@capacity,'');

LOAD DATA INFILE 'F:/University stage/Submission/CSV Files/ClubTableFinal.csv'
INTO TABLE Club
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(clubName,StadiumName,clubWebsite);

SET FOREIGN_KEY_CHECKS=0;
SET GLOBAL FOREIGN_KEY_CHECKS=0;

LOAD DATA INFILE 'F:/University stage/Submission/CSV Files/PlaysForTableFinalL.csv'
INTO TABLE PlayerInClubSeason
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(clubName, season,playerName, dateOfBirth);


LOAD DATA INFILE 'F:/University stage/Submission/CSV Files/MatchTableFinalL.csv'
INTO TABLE `Match`
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(homeClubName,awayClubName,season,matchDate,homePossessions,awayPossessions,homeShots,awayShots,homeYellowCard,awayYellowCard,homeFouls,awayFouls,homeRedCard,awayRedCard, homeGoals,awayGoals);

LOAD DATA INFILE 'F:/University stage/Submission/CSV Files/UserTableFinal.csv'
INTO TABLE `User`
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(userEmail,userName,`password`,gender,birthDate,favouriteClubName);

LOAD DATA INFILE 'F:/University stage/Submission/CSV Files/ReviewTableFinal.csv'
INTO TABLE UserMatchReview
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(userEmail,matchSeason,homeClubName,awayClubName,rating,textReview);


