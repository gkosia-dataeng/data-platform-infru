create table public.customers (
  customerid int, 
  name varchar(100),
  age int,
  balance decimal(18,2) 
        
);

create table public.orders (
   customerid int
  ,productId  varchar(100)
  ,create_date TIMESTAMP 
  ,amount decimal(18,2)
);



ALTER SYSTEM SET wal_level = logical;
ALTER SYSTEM SET max_wal_senders = 4;
ALTER SYSTEM SET max_replication_slots = 4;
SELECT pg_reload_conf();


