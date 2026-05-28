# Database creation and selection

create database consumer_analytics;
use consumer_analytics;

# Table creation queries 
create table train( id int, date date, store_nbr int, family varchar(100), sales float, onpromotion int);
CREATE TABLE stores (
    store_nbr INT,
    city VARCHAR(100),
    state VARCHAR(100),
    type CHAR(1),
    cluster INT
);
CREATE TABLE oil (
    date DATE,
    dcoilwtico FLOAT
);
CREATE TABLE holidays_events (
    date DATE,
    type VARCHAR(50),
    locale VARCHAR(50),
    locale_name VARCHAR(100),
    description VARCHAR(255),
    transferred BOOLEAN
);
CREATE TABLE transactions (
    date DATE,
    store_nbr INT,
    transactions INT
);

# Load data into tables
# loading data internally and externally 
LOAD DATA LOCAL INFILE 'C/:Users/shant/Desktop/NIQ_MARKETING_EFFECTIVENESS_PROJECT/Data/Raw/store-sales-time-series-forecasting/train.csv'
INTO TABLE train
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SET GLOBAL local_infile = 1;
use consumer_analytics;