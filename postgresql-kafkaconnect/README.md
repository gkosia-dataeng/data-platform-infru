# Postgresql-kafkaconnect
`Postgresql-kafkaconnect` deploying a postgresql instance and a kafka connect instance that will be used to replicate cdc to kafka

The app prerequisites the kafka-core to be running because kafka-connect is configured to write the cdc in kafka topics.
After the initiation of the app we have to register the connector using the kafka-connect rest api. The properties of the connector located in file `postgresql-register.json`


## Postgresql
The initial creation of the tables and the user used from kafka-connect exists in the sql file under the folder sql. Additional system settings required and configured in the sql file.


## Kafka-connect
 Kafka-connect will automatically create the destination topics if they are not exists. We can register connectors using the rest api.

## Start the environment from scratch

Open the terminal under the `postgresql-kafkaconnect` folder and execute:

```
# start kafka
docker-compose -f ../kafka-core/docker-compose.yml up -d 

# start postgresql and kafka-connect
docker-compose up -d

# register the connector using the properties file
curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @./postgresql-register.json


# connect to postgresql db
docker exec -it <postgresql container id> /bin/bash
psql -U root -d source_pg
```


In case a port is already binded, find the process that use the port:
``sudo lsof -t -i:5432``

