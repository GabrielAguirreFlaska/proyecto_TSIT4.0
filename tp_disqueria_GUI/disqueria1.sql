-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-11-2022 a las 14:34:26
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `disqueria1`
--
CREATE DATABASE disqueria1;
USE disqueria1;
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `album`
--

CREATE TABLE `album` (
  `id_album` int(11) NOT NULL,
  `cod_album` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `id_interprete` int(11) NOT NULL,
  `id_genero` int(11) NOT NULL,
  `cant_temas` int(11) NOT NULL,
  `id_discografica` int(11) NOT NULL,
  `id_formato` int(11) NOT NULL,
  `fec_lanzamiento` date DEFAULT NULL,
  `precio` double NOT NULL,
  `cantidad` int(11) NOT NULL,
  `caratula` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `album`
--

INSERT INTO `album` (`id_album`, `cod_album`, `nombre`, `id_interprete`, `id_genero`, `cant_temas`, `id_discografica`, `id_formato`, `fec_lanzamiento`, `precio`, `cantidad`, `caratula`) VALUES
(1, 1234567, 'Lêttre à ma Mère', 3, 5, 10, 5, 3, '1979-01-01', 1000, 2, NULL),
(2, 1234568, 'Las Cosas Que Vives', 1, 1, 12, 3, 1, '1996-01-01', 1000, 1, NULL),
(3, 1234569, 'En Tiempo de Amor', 2, 5, 10, 1, 1, '1993-01-01', 1000, 1, NULL),
(4, 1234570, 'El Piano de América', 2, 5, 10, 1, 1, '1994-01-01', 1000, 1, NULL),
(8, 123123123, 'xcvbxcvcb', 1, 1, 12, 1, 1, '0000-00-00', 122, 21212, ''),
(9, 567567, 'lalalaala', 13, 2, 12, 3, 3, '1998-02-25', 123, 10, ''),
(10, 2147483647, 'qewrqwrqwr', 3, 3, 2333333, 1, 1, '0000-00-00', 123, 12, ''),
(11, 324234, 'asdfadsfadsf', 1, 1, 23, 1, 1, '0000-00-00', 323, 333333, ''),
(12, 1212, 'nombre test 12', 4, 5, 1, 5, 4, '0000-00-00', 100, 10000000, ''),
(13, 12333, 'NN', 1, 1, 1212112, 1, 1, '0000-00-00', 123, 5467, ''),
(14, 123, 'No se', 25, 1, 14, 5, 1, '2022-11-05', 100, 100, ''),
(15, 124, 'No se 2', 25, 1, 15, 5, 1, '2022-11-05', 100, 100, ''),
(18, 99999, '99', 1, 1, 9, 1, 1, '0000-00-00', 0, 0, ''),
(19, 7, 'nombre nuevo', 1, 1, 7, 1, 1, '0000-00-00', 0, 0, ''),
(21, 3, '3333', 1, 1, 3, 1, 1, '2022-05-11', 3, 3, ''),
(22, 4, '', 1, 1, 3, 1, 1, '0000-00-00', 0, 0, '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `discografica`
--

CREATE TABLE `discografica` (
  `id_discografica` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `discografica`
--

INSERT INTO `discografica` (`id_discografica`, `nombre`) VALUES
(1, 'BMG'),
(2, 'Sony Music'),
(3, 'WEA'),
(4, 'Universal'),
(5, 'Independiente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `formato`
--

CREATE TABLE `formato` (
  `id_formato` int(11) NOT NULL,
  `tipo` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `formato`
--

INSERT INTO `formato` (`id_formato`, `tipo`) VALUES
(1, 'Compact Disc'),
(2, 'Cassette'),
(3, 'Long Play'),
(4, 'Digital');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `id_genero` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `genero`
--

INSERT INTO `genero` (`id_genero`, `nombre`) VALUES
(1, 'Pop'),
(2, 'Tango'),
(3, 'Bolero'),
(4, 'Folklore'),
(5, 'Instrumental'),
(6, 'Electrónica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `interprete`
--

CREATE TABLE `interprete` (
  `id_interprete` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `nacionalidad` varchar(50) DEFAULT NULL,
  `foto` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `interprete`
--

INSERT INTO `interprete` (`id_interprete`, `nombre`, `apellido`, `nacionalidad`, `foto`) VALUES
(1, 'Laura', 'Pausini', 'Italia', NULL),
(2, 'Raúl', 'DiBlasio', 'Argentina', NULL),
(3, 'Richard', 'Clayderman', 'Francia', NULL),
(4, 'Enya', 'Brennan', 'Irlanda', NULL),
(5, 'Vangelis', 'Papathanasiouss', 'Grecia', NULL),
(6, 'Jean Michel', 'Jarre', 'Francia', NULL),
(7, 'La Mona', 'Gimenez', 'Argentina', NULL),
(8, 'Chaqueño', 'Palavecino', 'Argentina', NULL),
(9, 'Hermanos', 'Pimpinela', 'Argentina', NULL),
(10, 'Ulises', 'Bueno', 'Argentina', NULL),
(11, 'Leo', 'Mattioli', 'Argentina', NULL),
(12, 'Carlos', 'Gardel', 'Argentina', NULL),
(13, 'Aztor', 'Piazzolla', 'Argentina', NULL),
(14, 'Michael', 'Jackson', 'USA', NULL),
(15, 'Luis Miguel', 'Gallego Basteri', 'Mexico', NULL),
(16, 'José Luis', 'Perales', 'España', NULL),
(17, 'Julio', 'Iglesias', 'España', NULL),
(18, 'Rosana', 'Arbelo Gopar', 'España', NULL),
(19, 'Indio', 'Solari', 'Argentina', 'Foto'),
(20, 'wwwwwww', 'qqqqqqqqqqqqqq', 'eeee', 'r'),
(21, 'rtrrtrtrtr', 'wer', 'yuiyui', 'Foto'),
(22, 'cccccc', 'c', 'c', 'c'),
(23, 'xxxxxxx', 'cxxxx', 'cxx', 'cx'),
(24, 'ttttttt', 'ttttt', 'tttt', 'ttt'),
(25, 'Gustavo3', 'Godoy3', 'Argentina', 'Foto3'),
(26, 'pepe', 'pepe', 'par', 'Foto'),
(28, 'zxzxzx', 'zxzxzx', 'zx', 'Foto'),
(29, 'ererer', 'erer', 'er', 'Foto'),
(30, 'ererer', 'erer', 'er', 'Foto'),
(31, 'qwqw', 'qw', 'qw', 'Foto'),
(32, 'qweqwe aaaaa', 'aaa', 'a', 'Foto'),
(33, '11111111111111', '222222', '3', 'Foto'),
(34, 'Otro nombre', 'otro apellido', 'asd', 'as'),
(35, 'nuevo nuevo', 'nuevo', 'n', 'Foto'),
(36, 'otro nuevo', 'nuevo apellido', 'Nacionalidad', 'Foto'),
(37, '678', '666777888', 'Nacionalidad', 'Foto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tema`
--

CREATE TABLE `tema` (
  `id_tema` int(11) NOT NULL,
  `titulo` varchar(100) DEFAULT NULL,
  `duracion` time DEFAULT NULL,
  `autor` varchar(100) NOT NULL,
  `compositor` varchar(100) NOT NULL,
  `id_album` int(11) DEFAULT NULL,
  `id_interprete` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tema`
--

INSERT INTO `tema` (`id_tema`, `titulo`, `duracion`, `autor`, `compositor`, `id_album`, `id_interprete`) VALUES
(1, 'Lêttre à ma Mère', '00:40:00', 'Paul De Senneville', 'Paul De Senneville', 1, 3),
(2, 'Mariage D\'Amour', '00:03:00', 'Paul De Senneville', 'Paul De Senneville', 1, 3),
(3, 'Souvenirs D\'Enfance', '00:03:00', 'Paul De Senneville', 'Paul De Senneville', 1, 3),
(4, 'Nostalgie', '00:03:00', 'Paul De Senneville', 'Paul De Senneville', 1, 3),
(9, '', '00:00:00', 'Autor', 'Compositor', 1, 1),
(10, 'nombre tema', '00:00:00', 'Autor ggggg', 'Compositor gggg', 10, 17),
(11, 'sdfgdfgdfsg', '00:00:00', 'Autor ggg 2', 'Compositor ggg 2', 9, 18),
(12, 'qweqweqweqweq', '01:45:00', 'Anonimo', 'Compositor anonimo', 10, 25),
(13, 'otro tema', '01:46:00', 'Anonimo 2', 'Compositor anonimo 2', 13, 25);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`id_album`),
  ADD KEY `id_genero` (`id_genero`),
  ADD KEY `id_discografica` (`id_discografica`),
  ADD KEY `id_formato` (`id_formato`);

--
-- Indices de la tabla `discografica`
--
ALTER TABLE `discografica`
  ADD PRIMARY KEY (`id_discografica`);

--
-- Indices de la tabla `formato`
--
ALTER TABLE `formato`
  ADD PRIMARY KEY (`id_formato`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id_genero`);

--
-- Indices de la tabla `interprete`
--
ALTER TABLE `interprete`
  ADD PRIMARY KEY (`id_interprete`);

--
-- Indices de la tabla `tema`
--
ALTER TABLE `tema`
  ADD PRIMARY KEY (`id_tema`),
  ADD KEY `id_album` (`id_album`),
  ADD KEY `id_interprete` (`id_interprete`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `album`
--
ALTER TABLE `album`
  MODIFY `id_album` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `discografica`
--
ALTER TABLE `discografica`
  MODIFY `id_discografica` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `formato`
--
ALTER TABLE `formato`
  MODIFY `id_formato` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id_genero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `interprete`
--
ALTER TABLE `interprete`
  MODIFY `id_interprete` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `tema`
--
ALTER TABLE `tema`
  MODIFY `id_tema` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `album`
--
ALTER TABLE `album`
  ADD CONSTRAINT `album_ibfk_1` FOREIGN KEY (`id_genero`) REFERENCES `genero` (`id_genero`),
  ADD CONSTRAINT `album_ibfk_2` FOREIGN KEY (`id_discografica`) REFERENCES `discografica` (`id_discografica`),
  ADD CONSTRAINT `album_ibfk_3` FOREIGN KEY (`id_formato`) REFERENCES `formato` (`id_formato`);

--
-- Filtros para la tabla `tema`
--
ALTER TABLE `tema`
  ADD CONSTRAINT `tema_ibfk_1` FOREIGN KEY (`id_album`) REFERENCES `album` (`id_album`),
  ADD CONSTRAINT `tema_ibfk_2` FOREIGN KEY (`id_interprete`) REFERENCES `interprete` (`id_interprete`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
