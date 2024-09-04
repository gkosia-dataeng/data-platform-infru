# Kafka-core
`Kafka-core` app deploying zookeeper and a kafka broker under the network `dataeng-data-platform` 

Broker internal port is `19092` and external is `9092`


```
kafka-topics --bootstrap-server kafka:19092 --list
kafka-topics --bootstrap-server kafka:19092 --create --topic skyone
kafka-topics --bootstrap-server kafka:19092 --create --topic sunset
kafka-topics --bootstrap-server kafka:19092 --create --topic flightdata
kafka-topics --bootstrap-server kafka:19092 --create --topic userstatistics


kafka-console-consumer --bootstrap-server kafka:19092 --topic skyone --from-beginning
kafka-console-consumer --bootstrap-server kafka:19092 --topic sunset --from-beginning

kafka-console-consumer --bootstrap-server kafka:19092 --topic flightdata --from-beginning
```