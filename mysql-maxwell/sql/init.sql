create database mysql_data;
use mysql_data;
create table customers(id int, name varchar(100), age int);
insert into customers values(1,'gab',33);
create table orders(id int, customer_id int, product_id int, amount int);
insert into orders values(1,1,1,1000);
insert into orders values(2,1,2,3);
