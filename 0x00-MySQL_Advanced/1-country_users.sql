-- Task 1
-- creates a table as the file 0 and add a new collumn
CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
