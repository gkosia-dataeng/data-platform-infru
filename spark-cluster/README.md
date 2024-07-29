# Spark Standalone Cluster

The `docker-compose` file initiates a spark cluster with one driver and two worker nodes.\
The worker nodes has been configured with 2 cores and 1Gb memory.

The cluster is deployed under the nework `dataeng-data-platform` to be combatible with all infrustructure in this repository.

After starting the cluster navigate to url `localhost:8080` to access the spark UI.\
In the spark UI you can find the cluster address to initiate a SparkSession.


To find the hadoop version that is used : login to container and `cd bitnami/spark/jars/` or `find / -type f -name '*hadoop*'`


## Libraries required to work with minIO(s3), delta tyables, hudi tables:
aws-java-sdk-bundle-1.12.367.jar  
hadoop-aws-3.3.6.jar  
delta-core_2.12-2.4.0.jar  
delta-storage-2.4.0.jar  
hudi-spark3.4-bundle_2.12-0.14.1.jar  
antlr4-runtime-4.9.3.jar  
wildfly-openssl-1.1.3.Final.jar


## Delete images related to the cluster
docker image rm $(docker images --filter=reference='spark-cluster*' --format '{{.Repository}}')

