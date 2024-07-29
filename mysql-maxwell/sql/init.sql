create database mysql_data;
use mysql_data;

create table customers (
  customerid int, 
  name varchar(100),
  age int,
  balance decimal(18,2) 
        
);

create table orders (
   customerid int
  ,productId  varchar(100)
  ,create_date datetime
  ,amount decimal(18,2)
);
