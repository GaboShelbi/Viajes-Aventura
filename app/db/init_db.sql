CREATE DATABASE IF NOT EXISTS viajes_aventura;
USE viajes_aventura;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);
