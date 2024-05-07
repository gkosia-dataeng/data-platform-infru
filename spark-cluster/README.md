# Spark Standalone Cluster

The `docker-compose` file initiates a spark cluster with one driver and two worker nodes.\
The worker nodes has been configured with 2 cores and 1Gb memory.

The cluster is deployed under the nework `dataeng-data-platform` to be combatible with all infrustructure in this repository.

After starting the cluster navigate to url `localhost:8080` to access the spark UI.\
In the spark UI you can find the cluster address to initiate a SparkSession.
