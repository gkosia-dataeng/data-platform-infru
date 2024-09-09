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

-- insert into public.deals values(1,111,1,'mt5','20240-10-01 10:15:00',1,1,100,0);
create table public.deals(
   deal_id INT
  ,platform_position_id INT
  ,login INT
  ,server varchar(100)
  ,execution_time TIMESTAMP 
  ,position_impact int
  ,trade_direction int
  ,volumn int
  ,profit int
);


-- insert into public.mt4account values(1, 'aaa',11)
CREATE TABLE public.mt4account(
   login INT 
  ,login_group varchar(100)
  ,user_id int
);

insert into public.mt4account values(1, 'aaa',11);
insert into public.deals values(1,111,1,'mt5','20240-10-01 10:15:00',2,1,100,10);


ALTER TABLE public.mt4account REPLICA IDENTITY FULL;

ALTER SYSTEM SET wal_level = logical;
ALTER SYSTEM SET max_wal_senders = 4;
ALTER SYSTEM SET max_replication_slots = 4;
SELECT pg_reload_conf();


