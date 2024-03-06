DROP USER IF EXISTS 'max';

CREATE USER 'max'@'%' IDENTIFIED WITH mysql_native_password BY 'maxwell';
GRANT ALL ON mysql_data.* TO 'max'@'%';


create database maxwell_metadata;
GRANT ALL ON maxwell_metadata.* TO 'max'@'%';

GRANT SELECT, REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'max'@'%';