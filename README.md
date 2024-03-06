# data-platform-infru
This repository contains docker-compose setups to build a data platform from open source tools
<br></br><br></br>
# Require
### **** Create the docker network to deploy all apps in the `dataeng-data-platform` 
```
docker network create dataeng-data-platform
```

### Apps 
[data-generator](./data-generator/): python scripts to push data in mysql, postgresql or kafka\
[kafka-core](./kafka-core/): zookeeper and kafka broker\
[minIO](./minIO): object storage, s3 compatible\
[mysql-maxwell](./mysql-maxwell): consume cdc from mysql using maxwell\
[postgresql-kafkaconnect](./postgresql-kafkaconnect/): consume cdc from postgresql using kafka connect\
[spark-cluster-mode](./spark-cluster-mode/): spark cluster with 2 worker nodes