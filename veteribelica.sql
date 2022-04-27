-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 27, 2022 at 11:55 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `veteribelica`
--

-- --------------------------------------------------------

--
-- Table structure for table `citas`
--

CREATE TABLE `citas` (
  `idcita` int(10) NOT NULL,
  `idanimal` int(10) NOT NULL,
  `fechaCreacion` varchar(255) COLLATE utf8_spanish_ci NOT NULL DEFAULT current_timestamp(),
  `fechaCita` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `citas`
--

INSERT INTO `citas` (`idcita`, `idanimal`, `fechaCreacion`, `fechaCita`) VALUES
(1, 1, '2022-04-25 22:54:08', '02 mayo'),
(2, 1, '2022-04-25 23:26:45', '2022-05-05'),
(3, 3, '2022-04-25 23:28:38', '2022-04-19'),
(4, 4, '2022-04-27 09:48:15', '2022-05-03'),
(5, 7, '2022-04-27 13:02:13', '2022-05-07');

-- --------------------------------------------------------

--
-- Table structure for table `mascotas`
--

CREATE TABLE `mascotas` (
  `idmascota` int(10) NOT NULL,
  `idusuario` int(10) NOT NULL,
  `nombreMascota` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `raza` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `mascotas`
--

INSERT INTO `mascotas` (`idmascota`, `idusuario`, `nombreMascota`, `raza`) VALUES
(1, 1, 'Rayo', 'belico'),
(2, 1, 'gary', 'gato'),
(3, 1, 'Clifford', 'Labrador'),
(4, 2, 'Wolfie', 'Danes'),
(5, 7, 'Sobrino', 'Gato'),
(6, 7, 'Federico', 'Cuyo'),
(7, 8, 'Rigoberto mayweather', 'Pollo');

-- --------------------------------------------------------

--
-- Table structure for table `recetas`
--

CREATE TABLE `recetas` (
  `idreceta` int(10) NOT NULL,
  `idanimal` int(10) NOT NULL,
  `fechareceta` date NOT NULL DEFAULT current_timestamp(),
  `prescripcion` text COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `recetas`
--

INSERT INTO `recetas` (`idreceta`, `idanimal`, `fechareceta`, `prescripcion`) VALUES
(1, 3, '2022-04-27', 'parecetamol'),
(2, 2, '2022-04-27', 'cariñitos'),
(3, 7, '2022-04-27', 'Caldo de pollo con requeson');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `idusuario` int(11) NOT NULL,
  `user` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `tipoUser` varchar(1) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`idusuario`, `user`, `password`, `tipoUser`) VALUES
(1, 'bernal', 'asd', 'S'),
(2, 'ely', 'asd', 'C'),
(3, 'Luis', 'asd', 'C'),
(4, 'Kini', 'asd', 'S'),
(5, 'amaro', 'asd', 'S'),
(6, 'farmin', 'asd', 'V'),
(7, 'mario', 'asd', 'C'),
(8, 'Pollo', 'asd', 'C');

-- --------------------------------------------------------

--
-- Table structure for table `ventas`
--

CREATE TABLE `ventas` (
  `idventa` int(10) NOT NULL,
  `insumo` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `cantidad` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `precio` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `fecha` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `ventas`
--

INSERT INTO `ventas` (`idventa`, `insumo`, `cantidad`, `precio`, `fecha`) VALUES
(1, 'tuki', '12', '1', '2022-04-27'),
(2, 'aimbot', '2', '300', '2022-04-27'),
(3, 'vandal tubitos', '2', '400', '2022-04-27');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `citas`
--
ALTER TABLE `citas`
  ADD PRIMARY KEY (`idcita`);

--
-- Indexes for table `mascotas`
--
ALTER TABLE `mascotas`
  ADD PRIMARY KEY (`idmascota`);

--
-- Indexes for table `recetas`
--
ALTER TABLE `recetas`
  ADD PRIMARY KEY (`idreceta`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idusuario`);

--
-- Indexes for table `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`idventa`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `citas`
--
ALTER TABLE `citas`
  MODIFY `idcita` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `mascotas`
--
ALTER TABLE `mascotas`
  MODIFY `idmascota` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `recetas`
--
ALTER TABLE `recetas`
  MODIFY `idreceta` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `ventas`
--
ALTER TABLE `ventas`
  MODIFY `idventa` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
