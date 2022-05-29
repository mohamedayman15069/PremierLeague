-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: premierleague
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `stadium`
--

DROP TABLE IF EXISTS `stadium`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stadium` (
  `stadiumName` varchar(55) NOT NULL,
  `addressPostalCode` varchar(15) NOT NULL,
  `addressCity` varchar(55) NOT NULL,
  `addressStreet` varchar(40) DEFAULT NULL,
  `buildingDate` int DEFAULT NULL,
  `lengthBitchSize` int NOT NULL,
  `widthBitchSize` int NOT NULL,
  `recordLeagueAttendance` int DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  PRIMARY KEY (`stadiumName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stadium`
--

LOCK TABLES `stadium` WRITE;
/*!40000 ALTER TABLE `stadium` DISABLE KEYS */;
INSERT INTO `stadium` VALUES ('Amex Stadium',' BN1 9BL','Brighton',' Village Way',2011,105,68,30565,30666),('Anfield',' L4 0TH','Liverpool',' Anfield Road',1884,101,68,53292,53394),('Bramall Lane',' S2 4SU',' Sheffield','Bramall Lane',1855,102,66,68287,32050),('Brentford Community Stadium',' TW8 0RU','Brentford',' Lionel Road South',2020,105,68,17094,17250),('Cardiff City Stadium',' CF11 8AZ','Cardiff',' Leckwith Road',2009,105,68,32321,33316),('Carrow Road',' NR1 1JE','Norwich',' Carrow Road',1935,104,68,27244,27359),('Craven Cottage',' SW6 6HH','London',' Stevenage Road',1896,100,65,19359,19000),('Elland Road',' LS11 0ES','Leeds',' Elland Road',1897,106,69,57892,37890),('Emirates Stadium',' N5 1BU','London',' 75 Drayton Park',2006,105,68,60161,60260),('Etihad Stadium',' M11 3FF','Manchester',' Etihad Campus',2002,105,68,54693,55017),('Goodison Park',' L4 4EL','Liverpool',' Goodison Road',1892,100,68,40552,39221),('John Smith\'s Stadium',' HD1 6PX','Huddersfield',' Stadium Way',1994,106,68,24426,24169),('King Power Stadium',' LE2 7FL','Leicester',' Filbert Way',2002,105,68,32242,32273),('London Stadium',' E20 2ST','London',' Queen Elizabeth Olympic Park',2011,105,68,59946,60000),('Molineux Stadium',' WV1 4QR','Wolverhampton',' Waterloo Rd',1889,105,68,31322,32050),('Old Trafford',' M16 0RA','Manchester',' Old Trafford',1909,105,68,76098,74879),('Selhurst Park',' SE25 6PU','London',' Holmesdale Road',1924,101,68,30115,25486),('St. James\' Park',' NE1 4ST','NewcastleUponTyne','St. James\' Park',1892,105,68,52490,52305),('St. Mary\'s Stadium',' SO14 5FP','Southampton',' Britannia Road',2001,105,68,32151,32384),('Stamford Bridge',' SW6 1HS','London',' Fulham Road',1877,103,67,42332,40853),('The Hawthorns',' B71 4LF',' West Bromwich','Halfords Ln',1900,105,68,27751,26688),('Tottenham Hotspur Stadium',' N17 0BX','London','782 High Rd',2019,100,67,61104,62062),('Turf Moor',' BB10 4BX',' Burnley','52-56 Harry Potts Way',1883,105,68,21870,21944),('Vicarage Road',' WD18 0ER','Hertfordshire',' Watford',1922,105,68,21590,21000),('Villa Park',' B6 6HE','Birmingham',' Trinity Road',1897,105,68,42045,42682),('Vitality Stadium',' BH7 7AF','Bournemouth',' Dean Court Rd',1910,105,68,11459,11329),('Wembley Stadium',' HA9 0WS','London','Rutherford Way',2007,105,68,85512,90000);
/*!40000 ALTER TABLE `stadium` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-11  1:29:09
