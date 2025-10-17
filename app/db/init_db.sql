CREATE DATABASE IF NOT EXISTS viajes_aventura;
USE viajes_aventura;

-- Tabla de usuarios con rol
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'cliente') NOT NULL DEFAULT 'cliente'
);

-- Tabla de destinos
CREATE TABLE IF NOT EXISTS destinos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    actividades TEXT NOT NULL,
    costo DECIMAL(10, 2) NOT NULL
);

-- Tabla de paquetes turísticos
CREATE TABLE IF NOT EXISTS paquetes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL
);

-- Tabla de relación muchos-a-muchos entre paquetes y destinos
CREATE TABLE IF NOT EXISTS paquete_destino (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paquete_id INT NOT NULL,
    destino_id INT NOT NULL,
    FOREIGN KEY (paquete_id) REFERENCES paquetes(id) ON DELETE CASCADE,
    FOREIGN KEY (destino_id) REFERENCES destinos(id) ON DELETE CASCADE
);

-- Tabla de reservas
CREATE TABLE IF NOT EXISTS reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    paquete_id INT NOT NULL,
    fecha_reserva DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (paquete_id) REFERENCES paquetes(id) ON DELETE CASCADE
);