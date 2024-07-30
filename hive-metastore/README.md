# Hive metastore
Hive metastore used to store the metadata about lakehouse table formats.
The `docker-compose` file will create two containers, one postgres database which is the backend of hive metastore and one container for the Hive.

The reference address for the metastore is `//hive-metastore:9083`


The jars needed to integrate with the minIO (s3) service stored in `./hadoop-libs` folder and they are mounted on hive container under the folder `/opt/hive/lib`


The connection details and configuration paths listed in file `./hive-config/hive-site.xml`


# How to use it

Run the command `docker-compose up -d` to start the hive metastore.