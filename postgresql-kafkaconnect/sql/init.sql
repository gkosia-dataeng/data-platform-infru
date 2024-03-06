create table public.product(id int, name varchar(100), category varchar(100));
insert into public.product values(1,'car','vehicles');
insert into public.product values(2,'apple','fruits');


ALTER SYSTEM SET wal_level = logical;
ALTER SYSTEM SET max_wal_senders = 4;
ALTER SYSTEM SET max_replication_slots = 4;
SELECT pg_reload_conf();


