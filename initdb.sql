CREATE DATABASE sportsclub;

USE sportsclub;

CREATE TABLE location(
	locId INT NOT NULL AUTO_INCREMENT,
   location varchar(255) DEFAULT NULL,
   PRIMARY KEY (locId)
   );    

CREATE TABLE members(
	memberId INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(255) DEFAULT NULL,
   age INT DEFAULT NULL, 
   email VARCHAR(255) DEFAULT NULL,
   gender ENUM('M','F') DEFAULT NULL, 
   locId INT DEFAULT NULL,
   PRIMARY KEY (memberId),
   FOREIGN KEY (locId) REFERENCES location(locId)
   );

CREATE TABLE admin(
	adminId INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(255) DEFAULT NULL,
   password varchar(255) DEFAULT NULL,   
   PRIMARY KEY (adminId)   
   );

CREATE TABLE stock(
	stockId INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(255) DEFAULT NULL, 
   description varchar(255) DEFAULT NULL,
   price FLOAT(10, 2),
   PRIMARY KEY (stockId)
   );    


INSERT INTO location (location) VALUES ("galway");
INSERT INTO location (location) VALUES ("cork");
INSERT INTO location (location) VALUES ("dublin");

INSERT INTO members (name, gender, locId, age) VALUES ("mary", "F", 1, 20);
INSERT INTO members (name, gender, locId, age) VALUES ("joe", "M", 2, 30);
INSERT INTO members (name, gender, locId, age) VALUES ("john", "M", 3, 40);

INSERT INTO stock (name, description, price) VALUES ("socks", "white with logo", 10.00);
INSERT INTO stock (name, description, price) VALUES ("bag", "black with logo", 30.00);
INSERT INTO stock (name, description, price) VALUES ("t-shirt", "cotton, white with logo", 20.00);

INSERT INTO admin (name) VALUES ("sheila");
INSERT INTO admin (name) VALUES ("nevin");