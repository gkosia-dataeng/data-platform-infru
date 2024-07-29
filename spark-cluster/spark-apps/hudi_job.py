from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("Test hudi job") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .config("spark.sql.extensions", "org.apache.spark.sql.hudi.HoodieSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.hudi.catalog.HoodieCatalog") \
    .config("spark.sql.catalogImplementation", "hive") \
    .config("spark.sql.warehouse.dir", "s3a://lakehouse/warehouse/hudi") \
    .getOrCreate()


data = [(1, "aa"), (2, "bb")]
headers = ["id", "name"]

df = spark.createDataFrame(data, headers)

hudi_unmanaged_options = {
  "hoodie.table.name": "hudi_unmanaged_table",
  "hoodie.datasource.write.operation" : "insert_overwrite"
}

# unmanaged table
df.write.format("hudi") \
  .options(**hudi_unmanaged_options) \
  .mode("overwrite")  \
  .save('s3a://lakehouse/warehouse/hudi/hudi_unmanaged_table')




# managed table 
spark.sql("CREATE DATABASE IF NOT EXISTS bronze;")
spark.sql("USE bronze;")

spark.sql("DROP TABLE IF EXISTS spark_catalog.bronze.hudi_mamaged_table;")


hudi_managed_options = {
  "hoodie.table.name": "hudi_mamaged_table",
  "hoodie.datasource.write.operation" : "insert_overwrite"
}


df.write.format("hudi") \
  .options(**hudi_managed_options) \
  .mode("overwrite")  \
  .saveAsTable('hudi_mamaged_table')

spark.sql('DESCRIBE TABLE EXTENDED hudi_mamaged_table;').show()
