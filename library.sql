-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2020 at 09:00 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `userid` int(10) NOT NULL,
  `username` varchar(50) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`userid`, `username`, `fname`, `lname`, `password`) VALUES
(1, 'saad', 'Saad', 'Islam', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `bookid` int(10) NOT NULL,
  `bookname` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `edition` varchar(50) NOT NULL,
  `published` year(4) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `book_status` int(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`bookid`, `bookname`, `author`, `edition`, `published`, `publisher`, `book_status`) VALUES
(5, 'Ma', 'Anisul Huq', '7th', 2003, 'Prothoma', 1),
(6, 'Ma', 'Anisul Huq', '7th', 2003, 'Prothoma', 0),
(7, 'ss', 'dd', 'ewr', 2001, 'sfsdf', 0),
(8, 'Data Structures and Algorithms, Volume 3', 'Kurt Mehlhorn', 'n/a', 1984, 'Springer-Verlag', 1),
(9, 'In Search of Lost Time', 'Marcel Proust', 'N/A', 1913, 'N/A', 0),
(10, 'The Prisoner: In Search of Lost Time, Volume 5', 'Carol Clark ', 'N/A', 0000, 'N/A', 0),
(11, 'The History of Tom Jones, a Foundling ', 'Henry Fielding', 'N/A', 0000, 'N/A', 0),
(12, 'The Red and the Black ', 'Stendhal', 'N/A', 0000, 'N/A', 0),
(13, 'War and Peace ', 'Tolstoy', 'N/A', 0000, 'N/A', 0),
(14, 'Madame Bovary', 'Gustave Flaubert', 'N/A', 0000, 'N/A', 0),
(15, 'Madame Bovary', 'Gustave Flaubert', 'N/A', 0000, 'N/A', 0),
(16, 'Madame Bovary', 'Gustave Flaubert', 'N/A', 0000, 'N/A', 1),
(17, 'Madame Bovary', 'Gustave Flaubert', 'N/A', 0000, 'N/A', 0),
(18, 'Madame Bovary', 'Gustave Flaubert', 'N/A', 0000, 'N/A', 0),
(19, 'A Game of Thrones', 'George R.R. Martin', '4th', 0000, 'N/A', 1),
(20, 'A Game of Thrones', 'George R.R. Martin', '4th', 0000, 'N/A', 0),
(21, 'A Game of Thrones', 'George R.R. Martin', '4th', 0000, 'N/A', 0),
(22, 'A Game of Thrones', 'George R.R. Martin', '4th', 0000, 'N/A', 1),
(23, 'Liza of Lambeth', 'William Somerset', '4th', 0000, 'N/A', 0),
(24, 'Ma', 'Anisul Huq', '4th', 2001, 'N/A', 0);

-- --------------------------------------------------------

--
-- Table structure for table `issuedbooks`
--

CREATE TABLE `issuedbooks` (
  `id` int(10) NOT NULL,
  `bookid` int(10) NOT NULL,
  `userid` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `issuedbooks`
--

INSERT INTO `issuedbooks` (`id`, `bookid`, `userid`) VALUES
(2, 8, 4),
(25, 16, 5),
(27, 5, 4),
(30, 19, 6),
(31, 22, 4);

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `userid` int(10) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(10) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact` varchar(15) NOT NULL,
  `dateregistered` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`userid`, `username`, `password`, `fname`, `lname`, `email`, `contact`, `dateregistered`) VALUES
(1, 'saad', '12345', 'Saad', 'Islam', 'noushinshoha@gmail.com', '01727567120', '2020-12-02'),
(3, 'ns', '224455', 'Noushin', 'Islam', 'ns@gmail.com', '01777788899', '2020-12-03'),
(4, 'lino', 'lino', 'Lino', 'Islam', 'as@gmail.com', '01788998844', '2020-12-01'),
(5, 'soikot', 'soikot', 'Soikot', 'Islam', 's@yahoo.com', '01700000000', '2020-10-15'),
(6, 'abu', 'horaira', 'Horaira', 'Islam', 'h@yahoo.com', '01700000000', '2020-10-18'),
(7, 'adnan101', 'adnan', 'Adnan', 'Huq', 'a@gmail.com', '01700000000', '2020-11-12'),
(8, 'nsaad', 'nsai', 'Noushin', 'Dewan', 'nis@gmail.com', '01733114477', '2020-12-12'),
(9, 'abir', 'abir', 'Abir', 'Islam', 'ab@gmail.com', '01700000000', '2020-10-15'),
(10, 'pial', 'pial', 'Pial', 'Roy', 'pi@gmail.com', '017888888', '2020-11-20'),
(11, 'niloy', 'niloy', 'Niloy', 'Barua', 'ni@gmail.com', '01788665544', '2019-12-12'),
(12, 'sdad', 'saad', 'Saad', 'Islam', 'najs@gmail.com', '01788000000', '2020-12-12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`userid`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`bookid`);

--
-- Indexes for table `issuedbooks`
--
ALTER TABLE `issuedbooks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`userid`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `userid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `bookid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `issuedbooks`
--
ALTER TABLE `issuedbooks`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `userid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
