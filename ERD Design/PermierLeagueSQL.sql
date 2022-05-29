CREATE SCHEMA IF NOT EXISTS `premierleague`;

CREATE TABLE IF NOT EXISTS Player(
	playerName varchar(50) NOT NULL, 
    dateOfBirth DATE , 
    nationality varchar(15), 
    weight int, 
    height int,
    `position` varchar(20) NOT NULL, 
	PRIMARY KEY (playerName, dateOfBirth)
);
CREATE TABLE IF NOT EXISTS Stadium(
	stadiumName varchar(55) NOT NULL PRIMARY KEY, 
    addressPostalCode varchar(15) NOT NULL, 
    addressCity varchar(15) NOT NULL, 
    addressStreet varchar(30), 
    buikdingDate char(4),  #years
    lengthBitchSize int NOT NULL, 
    widthBitchSize int NOT NULL,
    recordLeagueAttendance int, 
    capacity int
);

CREATE TABLE IF NOT EXISTS Club(
	clubName varchar(50) NOT NULL PRIMARY KEY, 
    clubWebsite varchar(100) NOT NULL,
	stadiumName varchar(55) NOT NULL, 
    constraint FK_stadiumClub FOREIGN KEY (stadiumName) REFERENCES Stadium (stadiumName)
    ON UPDATE CASCADE 
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS PlayerInClubSeason(
	playerName varchar(50) NOT NULL,
	clubName varchar(50) NOT NULL,
    dateOfBirth DATE NOT NULL, 
    season char(7) NOT NULL, 
    PRIMARY KEY (playerName, clubName, dateOfBirth, season),
    CONSTRAINT FK_player FOREIGN KEY (playerName, dateOfBirth)
    REFERENCES Player (playerName, dateOfBirth)
        ON UPDATE CASCADE ON DELETE CASCADE ,
    CONSTRAINT FK_club FOREIGN KEY(clubName) 
    REFERENCES Club(clubName)
    ON UPDATE CASCADE ON DELETE RESTRICT
);


CREATE TABLE IF NOT EXISTS `Match`(
	season char(7) NOT NULL, 
	stadiumName varchar(55) NOT NULL, 
	homeClubName varchar(50) NOT NULL,
	awayClubName varchar(50) NOT NULL,
	matchDate char(15) NOT NULL,
    homeRedCard int , 
    homePossessions decimal(2,1), 
    homeYellowCard int ,
    homeGoals int NOT NULL, 
    homeFouls int , 
    homeShots int , 
    awayRedCard int , 
    awayPossessions decimal(2,1) , 
    awayYellowCard int,
    awayGoals int NOT NULL, 
    awayFouls int, 
    awayShots int,
    PRIMARY KEY (season, homeClubName, awayClubName),
    constraint FK_MatchStadium FOREIGN KEY(stadiumName) REFERENCES Stadium(stadiumName)
    ON UPDATE CASCADE ON DELETE RESTRICT 
    ,
    constraint FK_MatchHomeClub FOREIGN KEY(homeClubName) REFERENCES Club(clubName)
    ON UPDATE CASCADE ON DELETE RESTRICT
    ,
    constraint FK_MatchAwayClub FOREIGN KEY(awayClubName) REFERENCES Club(clubName)
    ON UPDATE CASCADE ON DELETE RESTRICT 
);
CREATE TABLE IF NOT EXISTS `User`(
	userEmail varchar(40) NOT NULL PRIMARY KEY, 
    userName  varchar(30),
    `password`   CHAR(32) NOT NULL,
    gender      char(1) NOT NULL,
    birthDate   char(10) NOT NULL,
    favouriteClubName varchar(15) NOT NULL, 
    constraint FK_favClubName FOREIGN KEY (favouriteClubName) REFERENCES Club(clubName)
    ON UPDATE CASCADE ON DELETE RESTRICT 
);
CREATE TABLE IF NOT EXISTS UserMatchReview(
	userEmail varchar(40) NOT NULL, 
    matchSeason char(7) NOT NULL, 
	homeClubName varchar(50) NOT NULL,
	awayClubName varchar(50) NOT NULL,
	rating decimal(2,2) NOT NULL,
    textReview  varchar(1000) NOT NULL, 
    PRIMARY KEY (userEmail, matchSeason, homeClubName, awayClubName), 
       CONSTRAINT FK_MatchSeasons FOREIGN KEY (matchSeason) REFERENCES `Match`(season)
	 ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_userEmail FOREIGN KEY (userEmail) REFERENCES `User`(userEmail)
	 ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_homeClubName FOREIGN KEY (homeClubName) REFERENCES Club (clubName)
     ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FK_awayClubName FOREIGN KEY (awayClubName) REFERENCES Clplayerinclubseasonub (clubName)
    ON UPDATE CASCADE ON DELETE CASCADE
);

