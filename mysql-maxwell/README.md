## Mysql-maxwell

 `Mysql-maxwell` deploying a mysql instance and a maxwell instance that replicates the cdc to kafka.

The app prerequisites the kafka-core to be running because maxwell is configured to write the cdc in kafka topics. \
After the initiation of kafka components the script `create_required_topics.sh` should be run because maxwell needs the destination topics to already exists. 

All resources in this repo are deployed under the docker network `dataeng-data-platform` in order to communicate each other when deployed from different docker-compose files

### Mysql
The initial creation of the tables and the user used from maxwell exists in sql files under the folder `sql`


### Maxwell
The file config.properties contains the configuration of the maxwell instance. \
The configuration contains the user credentials of the user that will be used for replication, the topics and metadata database, and the filters of database/tables to monitor.

```
    

```
### Start the environment from scratch
Open the terminal under the `mysql-maxwell` folder and execute: 

```
# start kafka
docker-compose -f ../kafka-core/docker-compose.yml up -d 

# create target topics
bash ./create_required_topics.sh

# start mysql and maxwell
docker-compose up -d
```