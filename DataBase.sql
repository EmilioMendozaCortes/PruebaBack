CREATE DATABASE  IF NOT EXISTS `employees` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `employees`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: employees
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombres` varchar(80) NOT NULL,
  `Primer_Apellido` varchar(80) NOT NULL,
  `Segundo_Apellido` varchar(80) NOT NULL,
  `CURP` varchar(18) NOT NULL,
  `Puesto` varchar(45) DEFAULT NULL,
  `ClaveEmpleado` varchar(12) NOT NULL,
  `Calle` varchar(40) NOT NULL,
  `NoExterior` int NOT NULL,
  `NoInterior` int DEFAULT NULL,
  `Colonia` varchar(40) NOT NULL,
  `Municipio` varchar(40) NOT NULL,
  `Estado` varchar(50) NOT NULL,
  `Pais` varchar(47) NOT NULL,
  `Fecha_Registro` datetime NOT NULL,
  `Fecha_Actualizacion` datetime DEFAULT NULL,
  `Clave_Jefe_Inmediato` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `CURP` (`CURP`),
  KEY `Clave_Jefe_Inmediato` (`Clave_Jefe_Inmediato`),
  KEY `ix_Employees_ID` (`ID`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`Clave_Jefe_Inmediato`) REFERENCES `employees` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Yolanda','Perez','Juarez','YOPJ406979HPLERE15','CEO','YOPJ40697981','Mina',105,0,'Catarina','Huauchinango','Puebla','México','2024-10-20 10:48:12',NULL,NULL),(2,'Daniel','Martinez','Cruz','DAMC406979HPKERE12','Manager(Producction)','DAMC40697973','5 de Mayo',15,0,'Los angeles','Yujuslavia','CDMX','México','2024-10-20 10:48:43',NULL,1),(3,'Rocio','Dulce','Cruz','RODC406349HPKERE15','Operaciones','RODC40634995','Calderon',15,0,'Centro','La ceiba','Queretaro','México','2024-10-20 10:54:06',NULL,2),(4,'Luis','Asención','Valderrabano','LUAV406349HPKERE15','Diseño','LUAV40634945','Chiverria',65,1,'Centro','La ceiba','Nayarit','México','2024-10-20 10:55:40',NULL,2),(5,'Claudia','Santillan','Perez','CLSP403749HPKERE1A','Empleado','CLSP40374996','Chiverria',234,5,'Centro','La ceiba','Nuevo León','México','2024-10-20 10:58:44',NULL,3),(6,'Hector','Gonzales','Vazquez','HEGV403749ADKERE1A','Empleado','HEGV40374942','Cruz',23,0,'Centro','Cancun','Veracruz','México','2024-10-20 11:00:03',NULL,3),(7,'Jesus','Lopez','Gaona','JELG403749A6YERE1A','Empleado','JELG40374978','Milagro',93,0,'Centro','Cancun','Puebla','México','2024-10-20 11:01:28',NULL,4),(9,'Lucia','Maya','Cabrera','LUMC40374GA6YERE1A','Manager(Marketing)','LUMC40374G98','Dominicana',13,0,'Centro','Cancun','Baja California','México','2024-10-20 11:03:43',NULL,1),(10,'Miguel','Zavaleta','Torres','MIZT40374GA6T5RE1A','Ventas','MIZT40374G23','Colonias',13,0,'Uno','Cancun','Baja California Sur','México','2024-10-20 11:05:33',NULL,9),(11,'Rosana','Michell','Garrido','ROMG40374GA6T5RE1A','Comunicación','ROMG40374G40','Coahuila',56,0,'Uno','Cancun','Monterrey','México','2024-10-20 11:07:02',NULL,9),(12,'Alexandra','Gaona','Merida','ALGM403F4JA6T5RE1A','Empleado','ALGM403F4J60','Coahuila',56,0,'Uno','Merida','Monterrey','México','2024-10-20 11:08:36',NULL,10),(13,'Eva','Luna','Sol','EVLS703F4JA6T5RE1A','Empleado','EVLS703F4J11','Luxemburgo',46,0,'Uno','Merida','Monterrey','México','2024-10-20 11:09:41',NULL,11),(14,'Jose Ramón','Zoto','Ibarra','JOZI703F4JAJT5RE1A','Empleado','JOZI703F4J24','Colima',46,0,'Uno','Merida','Queretaro','México','2024-10-20 11:10:45',NULL,11);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'employees'
--

--
-- Dumping routines for database 'employees'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-20  5:12:23
