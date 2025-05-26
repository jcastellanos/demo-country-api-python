CREATE DATABASE IF NOT EXISTS demo_kubernetes;
USE demo_kubernetes;

CREATE TABLE IF NOT EXISTS country (
    code VARCHAR(2) PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO country (code, name) VALUES
('US', 'United States'),
('MX', 'Mexico'),
('CA', 'Canada'),
('ES', 'Spain'),
('FR', 'France'),
('DE', 'Germany'),
('IT', 'Italy'),
('UK', 'United Kingdom'),
('JP', 'Japan'),
('CN', 'China');
