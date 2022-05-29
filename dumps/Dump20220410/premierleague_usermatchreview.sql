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
-- Table structure for table `usermatchreview`
--

DROP TABLE IF EXISTS `usermatchreview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usermatchreview` (
  `userEmail` varchar(40) NOT NULL,
  `matchSeason` char(7) NOT NULL,
  `homeClubName` varchar(50) NOT NULL,
  `awayClubName` varchar(50) NOT NULL,
  `rating` decimal(2,2) NOT NULL,
  `textReview` varchar(1000) NOT NULL,
  PRIMARY KEY (`userEmail`,`matchSeason`,`homeClubName`,`awayClubName`),
  KEY `FK_MatchSeasons` (`matchSeason`),
  KEY `FK_homeClubName` (`homeClubName`),
  KEY `FK_awayClubName` (`awayClubName`),
  CONSTRAINT `FK_awayClubName` FOREIGN KEY (`awayClubName`) REFERENCES `club` (`clubName`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_homeClubName` FOREIGN KEY (`homeClubName`) REFERENCES `club` (`clubName`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_MatchSeasons` FOREIGN KEY (`matchSeason`) REFERENCES `match` (`season`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_userEmail` FOREIGN KEY (`userEmail`) REFERENCES `user` (`userEmail`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usermatchreview`
--

LOCK TABLES `usermatchreview` WRITE;
/*!40000 ALTER TABLE `usermatchreview` DISABLE KEYS */;
INSERT INTO `usermatchreview` VALUES ('mohamedayman15069@aucegypt.edu','21/2020','Arsenal','Manchester City',0.60,'Good Match');
/*!40000 ALTER TABLE `usermatchreview` ENABLE KEYS */;
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
