show databases;
use sports;
show tables;
select * from chess;
CREATE TABLE IF NOT EXISTS CHESSGMFORM (
    SL_NO INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    Gender VARCHAR(20),
    Title VARCHAR(20),
    Year_of_Title INT,
    Salary INT,
    City VARCHAR(50)
);
select * from chessgmform;

