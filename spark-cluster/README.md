# Spark Standalone Cluster

This `docker-compose.yml` file initiates a Spark cluster with one driver and two worker nodes. Each worker node is configured with 2 cores and 1 GB of memory.

The cluster is deployed under the `dataeng-data-platform` network to ensure compatibility with all the other infrastructure in this repository.

## Instructions

1. **Start the Spark Cluster:**
   
   To start the cluster, run the following command in the directory containing your `docker-compose.yml` file:
   `   docker-compose up -d`

# Testing the cluster

After starting the cluster in Docker, you can verify that it is running correctly by executing the following command:
`docker ps`. \
You should see three containers listed: one for the master node and two for the worker nodes.


Under the folder `spark-apps` there are some test jobs.
To run the jobs, login to master node using the command `docker exec -it spark-master /bin/bash`

From the master node, navigate to the spark-apps directory `cd ../../spark-apps` and execute the desired job using the appropriate spark-submit command `spark-submit delta_job.py`.

Some of the test jobs are writting to data lake so before you execute that kind of job start the minIO (data lake app) and Hive (metastore) containers.
```
    # start the minIO
    docker-compose -f ../minIO/docker-compose.yml up -d

    # start the Hive metastore
    docker-compose -f ../hive-metastore/docker-compose.yml up -d

```



## Libraries required to work with minIO(s3), delta tyables, hudi tables:
To keep this repository lightweight, the necessary JAR files are not included. Download the JAR files listed below and place them in the `./jars` directory.

```
aws-java-sdk-bundle-1.12.367.jar  
hadoop-aws-3.3.6.jar  
delta-core_2.12-2.4.0.jar  
delta-storage-2.4.0.jar  
hudi-spark3.4-bundle_2.12-0.14.1.jar  
antlr4-runtime-4.9.3.jar  
wildfly-openssl-1.1.3.Final.jar
```

To find the hadoop version that is used : login to container and `cd bitnami/spark/jars/` or `find / -type f -name '*hadoop*'`


## Delete images related to the cluster
docker image rm $(docker images --filter=reference='spark-cluster*' --format '{{.Repository}}')
