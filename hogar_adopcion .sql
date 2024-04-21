-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-01-2024 a las 15:01:25
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `adopciones`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hogar_adopcion`
--

CREATE TABLE `hogar_adopcion` (
  `especie` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `edad` int(255) NOT NULL,
  `tamaño` varchar(255) NOT NULL,
  `raza` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `numero_chip` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='para insertar los valores de mascota';

--
-- Volcado de datos para la tabla `hogar_adopcion`
--

INSERT INTO `hogar_adopcion` (`especie`, `color`, `edad`, `tamaño`, `raza`, `nombre`, `numero_chip`) VALUES
('Mamifero', 'cafe', 12, 'Grande', 'Chiguagua', 'Sussy', 4567823),
('Mamifero', 'blanco y negro', 3, 'mediamo', 'Pugg', 'Tuty', 827364),
('Ave', 'verde on plumas rojas', 5, 'Peuqeño', 'Loro Choroi', 'Pepito', 58659374),
('Ave', 'verde', 6, 'Mediano', 'Tucan', 'Tucancito', 857482934),
('Mamifero', 'cafe', 12, 'Grande', 'Chiguagua', 'Sussy', 4567823),
('Mamifero', 'blanco y negro', 3, 'mediamo', 'Pugg', 'Tuty', 827364),
('Ave', 'verde on plumas rojas', 5, 'Peuqeño', 'Loro Choroi', 'Pepito', 58659374),
('Ave', 'verde', 6, 'Mediano', 'Tucan', 'Tucancito', 857482934),
('Mamifero', 'Blanco', 4, 'Grande', 'Caballo de las maontañas', 'Alex', 78645643),
('Mamifero', 'rosado', 6, 'grande', 'chancho', 'piggy', 94859473),
('Mamifero', 'cafe', 12, 'Grande', 'Chiguagua', 'Sussy', 4567823),
('Mamifero', 'blanco y negro', 3, 'mediamo', 'Pugg', 'Tuty', 827364),
('Ave', 'verde on plumas rojas', 5, 'Peuqeño', 'Loro Choroi', 'Pepito', 58659374),
('Ave', 'verde', 6, 'Mediano', 'Tucan', 'Tucancito', 857482934),
('Mamifero', 'cafe', 12, 'Grande', 'Chiguagua', 'Sussy', 4567823),
('Mamifero', 'blanco y negro', 3, 'mediamo', 'Pugg', 'Tuty', 827364),
('Ave', 'verde on plumas rojas', 5, 'Peuqeño', 'Loro Choroi', 'Pepito', 58659374),
('Ave', 'verde', 6, 'Mediano', 'Tucan', 'Tucancito', 857482934),
('Mamifero', 'Blanco', 4, 'Grande', 'Caballo de las maontañas', 'Alex', 78645643),
('Mamifero', 'rosado', 6, 'grande', 'chancho', 'piggy', 94859473),
('Mamifero', 'cafe', 12, 'Grande', 'Chiguagua', 'Sussy', 4567823),
('Mamifero', 'blanco y negro', 3, 'mediamo', 'Pugg', 'Tuty', 827364),
('Ave', 'verde on plumas rojas', 5, 'Peuqeño', 'Loro Choroi', 'Pepito', 58659374),
('Ave', 'verde', 6, 'Mediano', 'Tucan', 'Tucancito', 857482934),
('Mamifero', 'cafe', 12, 'Grande', 'Chiguagua', 'Sussy', 4567823),
('Mamifero', 'blanco y negro', 3, 'mediamo', 'Pugg', 'Tuty', 827364),
('Ave', 'verde on plumas rojas', 5, 'Peuqeño', 'Loro Choroi', 'Pepito', 58659374),
('Ave', 'verde', 6, 'Mediano', 'Tucan', 'Tucancito', 857482934),
('Mamifero', 'Blanco', 4, 'Grande', 'Caballo de las maontañas', 'Alex', 78645643),
('Mamifero', 'rosado', 6, 'grande', 'chancho', 'piggy', 94859473),
('Mamifero', 'cafe', 12, 'Grande', 'Chiguagua', 'Sussy', 4567823),
('Mamifero', 'blanco y negro', 3, 'mediamo', 'Pugg', 'Tuty', 827364),
('Ave', 'verde on plumas rojas', 5, 'Peuqeño', 'Loro Choroi', 'Pepito', 58659374),
('Ave', 'verde', 6, 'Mediano', 'Tucan', 'Tucancito', 857482934),
('Mamifero', 'cafe', 12, 'Grande', 'Chiguagua', 'Sussy', 4567823),
('Mamifero', 'blanco y negro', 3, 'mediamo', 'Pugg', 'Tuty', 827364),
('Ave', 'verde on plumas rojas', 5, 'Peuqeño', 'Loro Choroi', 'Pepito', 58659374),
('Ave', 'verde', 6, 'Mediano', 'Tucan', 'Tucancito', 857482934),
('Mamifero', 'Blanco', 4, 'Grande', 'Caballo de las maontañas', 'Alex', 78645643),
('Mamifero', 'rosado', 6, 'grande', 'chancho', 'piggy', 94859473);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
