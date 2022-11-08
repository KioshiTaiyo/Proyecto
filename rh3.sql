-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-10-2022 a las 15:15:45
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
-- Base de datos: `rh3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `area`
--

CREATE TABLE `area` (
  `idArea` int(5) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `area`
--

INSERT INTO `area` (`idArea`, `descripcion`) VALUES
(1, 'Programación'),
(2, 'Programación 2'),
(3, 'Programación 3'),
(4, 'Programación 4'),
(5, 'Programación 5');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrera`
--

CREATE TABLE `carrera` (
  `idCarrera` int(5) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `carrera`
--

INSERT INTO `carrera` (`idCarrera`, `descripcion`) VALUES
(1, 'Soporte y Mantenimiento de Equipo de Computo'),
(2, 'Soporte y Mantenimiento de Equipo de Computo 2'),
(3, 'Soporte y Mantenimiento de Equipo de Computo 3'),
(4, 'Soporte y Mantenimiento de Equipo de Computo 4'),
(5, 'Soporte y Mantenimiento de Equipo de Computo 5');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escolaridad`
--

CREATE TABLE `escolaridad` (
  `idEscolaridad` int(5) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `escolaridad`
--

INSERT INTO `escolaridad` (`idEscolaridad`, `descripcion`) VALUES
(1, 'Preparatoria'),
(2, 'Universidad'),
(3, ' Preparatoria 2'),
(4, 'Preparatoria 3'),
(5, 'Preparatoria 4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadocivil`
--

CREATE TABLE `estadocivil` (
  `idEstadocivil` int(5) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estadocivil`
--

INSERT INTO `estadocivil` (`idEstadocivil`, `descripcion`) VALUES
(1, 'soltero'),
(2, 'casado'),
(3, 'Unión libre'),
(4, 'Soltero 2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gradoavance`
--

CREATE TABLE `gradoavance` (
  `idGradoavance` int(5) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `gradoavance`
--

INSERT INTO `gradoavance` (`idGradoavance`, `descripcion`) VALUES
(1, 'Preparatoria'),
(2, 'Preparatoria 2'),
(3, 'Preparatoria 3'),
(4, 'Preparatoria 4'),
(5, 'Preparatoria 5');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habilidades`
--

CREATE TABLE `habilidades` (
  `idHabilidades` int(5) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `habilidades`
--

INSERT INTO `habilidades` (`idHabilidades`, `descripcion`) VALUES
(1, 'No requerido'),
(2, 'Dibujar 2'),
(3, 'Dibujar 3'),
(4, 'Dibujar 4'),
(5, 'Dibujar 5');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `idioma`
--

CREATE TABLE `idioma` (
  `idIdioma` int(5) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `idioma`
--

INSERT INTO `idioma` (`idIdioma`, `descripcion`) VALUES
(1, 'No requerido'),
(2, 'Francés'),
(3, 'Alemán'),
(4, 'Italiano'),
(5, 'Mandarín');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mediopublicidad`
--

CREATE TABLE `mediopublicidad` (
  `idMediopublicidad` int(5) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto`
--

CREATE TABLE `puesto` (
  `idPuesto` int(11) NOT NULL,
  `codPuesto` varchar(15) NOT NULL,
  `idArea` int(11) NOT NULL,
  `nomPuesto` varchar(50) NOT NULL,
  `puestoJefeSup` varchar(50) NOT NULL,
  `jornada` varchar(70) NOT NULL,
  `remunMensual` int(11) NOT NULL,
  `prestaciones` varchar(70) NOT NULL,
  `descripcionGeneral` varchar(250) NOT NULL,
  `funciones` varchar(250) NOT NULL,
  `edad` varchar(50) NOT NULL,
  `sexo` varchar(15) NOT NULL,
  `idEstadoCivil` int(11) NOT NULL,
  `idEscolaridad` int(11) NOT NULL,
  `idGradoAvance` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `experiencia` varchar(70) NOT NULL,
  `conocimientos` varchar(70) NOT NULL,
  `manejoEquipo` varchar(70) NOT NULL,
  `reqFisicos` varchar(70) NOT NULL,
  `reqPsicologicos` varchar(70) NOT NULL,
  `responsabilidades` varchar(70) NOT NULL,
  `condicionesTrabajo` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `puesto`
--

INSERT INTO `puesto` (`idPuesto`, `codPuesto`, `idArea`, `nomPuesto`, `puestoJefeSup`, `jornada`, `remunMensual`, `prestaciones`, `descripcionGeneral`, `funciones`, `edad`, `sexo`, `idEstadoCivil`, `idEscolaridad`, `idGradoAvance`, `idCarrera`, `experiencia`, `conocimientos`, `manejoEquipo`, `reqFisicos`, `reqPsicologicos`, `responsabilidades`, `condicionesTrabajo`) VALUES
(1, 'v666', 3, 'Obrero', 'wefkq', 'qrqwe', 10000, 'qwerfw', 'wqerqwe', 'sdaftttttf', 'de 18 a 45 años', 'Hombre', 1, 4, 3, 1, 'no necesaria', 'Programación', 'computo', 'no necesarios', 'no necesarios', 'kdfeaf', 'óptimas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_habilidad`
--

CREATE TABLE `puesto_has_habilidad` (
  `idPuesto` int(11) NOT NULL,
  `idHabilidades` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_idioma`
--

CREATE TABLE `puesto_has_idioma` (
  `idPuesto` int(11) NOT NULL,
  `idIdioma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `puesto_has_idioma`
--

INSERT INTO `puesto_has_idioma` (`idPuesto`, `idIdioma`) VALUES
(1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `requisicion`
--

CREATE TABLE `requisicion` (
  `idRequisicion` int(11) NOT NULL,
  `folio` varchar(25) NOT NULL,
  `fechaElab` date NOT NULL,
  `fechaRecluta` date NOT NULL,
  `fechaInicVac` date NOT NULL,
  `motivoRequisicion` varchar(30) NOT NULL,
  `motivoEspecifique` varchar(70) NOT NULL,
  `tipoVacante` varchar(15) NOT NULL,
  `nomSolicita` varchar(70) NOT NULL,
  `nomAutoriza` varchar(70) NOT NULL,
  `nomRevisa` varchar(70) NOT NULL,
  `autorizada` tinyint(1) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  `idArea` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `requisicion`
--

INSERT INTO `requisicion` (`idRequisicion`, `folio`, `fechaElab`, `fechaRecluta`, `fechaInicVac`, `motivoRequisicion`, `motivoEspecifique`, `tipoVacante`, `nomSolicita`, `nomAutoriza`, `nomRevisa`, `autorizada`, `idPuesto`, `idArea`) VALUES
(1, 'A1', '2005-03-11', '2004-06-05', '2006-05-04', '', '', 'Temporal', 'Angel', 'mi', 'yo', 1, 1, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`idArea`);

--
-- Indices de la tabla `carrera`
--
ALTER TABLE `carrera`
  ADD PRIMARY KEY (`idCarrera`);

--
-- Indices de la tabla `escolaridad`
--
ALTER TABLE `escolaridad`
  ADD PRIMARY KEY (`idEscolaridad`);

--
-- Indices de la tabla `estadocivil`
--
ALTER TABLE `estadocivil`
  ADD PRIMARY KEY (`idEstadocivil`);

--
-- Indices de la tabla `gradoavance`
--
ALTER TABLE `gradoavance`
  ADD PRIMARY KEY (`idGradoavance`);

--
-- Indices de la tabla `habilidades`
--
ALTER TABLE `habilidades`
  ADD PRIMARY KEY (`idHabilidades`);

--
-- Indices de la tabla `idioma`
--
ALTER TABLE `idioma`
  ADD PRIMARY KEY (`idIdioma`);

--
-- Indices de la tabla `mediopublicidad`
--
ALTER TABLE `mediopublicidad`
  ADD PRIMARY KEY (`idMediopublicidad`);

--
-- Indices de la tabla `puesto`
--
ALTER TABLE `puesto`
  ADD PRIMARY KEY (`idPuesto`),
  ADD KEY `idEscolaridad` (`idEscolaridad`),
  ADD KEY `idEstadoCivil` (`idEstadoCivil`),
  ADD KEY `idGradoAvance` (`idGradoAvance`),
  ADD KEY `idCarrera` (`idCarrera`),
  ADD KEY `area` (`idArea`);

--
-- Indices de la tabla `puesto_has_habilidad`
--
ALTER TABLE `puesto_has_habilidad`
  ADD PRIMARY KEY (`idHabilidades`,`idPuesto`),
  ADD KEY `idHabilidades` (`idHabilidades`);

--
-- Indices de la tabla `puesto_has_idioma`
--
ALTER TABLE `puesto_has_idioma`
  ADD PRIMARY KEY (`idPuesto`,`idIdioma`),
  ADD KEY `idIdioma` (`idIdioma`);

--
-- Indices de la tabla `requisicion`
--
ALTER TABLE `requisicion`
  ADD PRIMARY KEY (`idRequisicion`),
  ADD KEY `idPuesto` (`idPuesto`),
  ADD KEY `idArea` (`idArea`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `area`
--
ALTER TABLE `area`
  MODIFY `idArea` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `carrera`
--
ALTER TABLE `carrera`
  MODIFY `idCarrera` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `escolaridad`
--
ALTER TABLE `escolaridad`
  MODIFY `idEscolaridad` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `estadocivil`
--
ALTER TABLE `estadocivil`
  MODIFY `idEstadocivil` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `gradoavance`
--
ALTER TABLE `gradoavance`
  MODIFY `idGradoavance` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `habilidades`
--
ALTER TABLE `habilidades`
  MODIFY `idHabilidades` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `idioma`
--
ALTER TABLE `idioma`
  MODIFY `idIdioma` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `mediopublicidad`
--
ALTER TABLE `mediopublicidad`
  MODIFY `idMediopublicidad` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `puesto`
--
ALTER TABLE `puesto`
  MODIFY `idPuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `puesto_has_idioma`
--
ALTER TABLE `puesto_has_idioma`
  MODIFY `idPuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `requisicion`
--
ALTER TABLE `requisicion`
  MODIFY `idRequisicion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
