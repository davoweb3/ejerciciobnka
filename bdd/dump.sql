-- --------------------------------------------------------
-- Host:                         sql10.freemysqlhosting.net
-- Versión del servidor:         5.5.62-0ubuntu0.14.04.1 - (Ubuntu)
-- SO del servidor:              debian-linux-gnu
-- HeidiSQL Versión:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla sql10677641.account: ~0 rows (aproximadamente)

-- Volcando datos para la tabla sql10677641.user: ~15 rows (aproximadamente)
REPLACE INTO `user` (`id`, `nombres`, `email`, `username`, `password`, `cuenta`, `saldo`) VALUES
	(36, 'El Toto33333', 'arf@ejemp333lo.com', 'eltoto_232232', 'contraseña', '1234567ee0', 1000),
	(38, 'El Toto377773333', 'arf@ejemp3337777lo.com', 'eltoto_2327777777723', 'contraseña', '1234777567ee0', 1000),
	(43, 'Raton2', '', '', '', '', NULL),
	(48, 'Pepe Trueno', 'recargado@ejemplo.com', 'edgarr23', '1238953', '1000745712', 14000),
	(49, 'Ironman Naula', 'cobaya202ss2@gmail.com', 'edgarr2ss3', '123895ss3', '100074430987', 14800),
	(50, 'Pink Floyd', 'pink@gmail.com', 'pinkfloyd', '123895ww3', '10003314', 2075.5),
	(54, 'LOCO VALDEZ', 'locoloco@gmail.com', 'locovaldez', '12345', '1716573314', 150),
	(55, 'DAVID RAMIREZ MATAMOROS', 'cedatos@mi.com', 'davicho2024', '12345', '1452', 20),
	(59, 'CESAR RAMIREZ', 'dodo@gmail.com', 'david', '123456', '1231231', 100),
	(60, 'FULGENCIO REALPE', 's@gmail.com', 'drone', '12345', '123123123', 1),
	(64, 'FULGENCIO REALPE', 's2@gmail.com', 'drone2', '12345', '123123123222', 1),
	(67, 'CESAR RAMIREZ', 'ye2sye@gmail.com', 'elzorrodel922', '12345', '12312322222', 45),
	(73, 'Lorenzo Izurieta', 'lor@gmail.com', 'lorenzo', '12345', '17165733', 150);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
