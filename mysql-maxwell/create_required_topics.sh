kafka-topics.sh --bootstrap-server localhost:9092 --topic cdc_mysql_data_customers --create 
kafka-topics.sh --bootstrap-server localhost:9092 --topic cdc_mysql_data_orders --create 
kafka-topics.sh --bootstrap-server localhost:9092 --topic mysql_ddl --create 