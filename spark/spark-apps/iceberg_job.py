from pyspark.sql import SparkSession


spark = (
            SparkSession.
             builder.
             appName("iceberg").
             config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"). 
             config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkCatalog"). 
             config("spark.sql.catalogImplementation", "hive"). 
             config("spark.sql.warehouse.dir", "s3a://lakehouse/warehouse/iceberg").
             getOrCreate()    
)


data = [(1, "aa"), (2, "bb")]
headers = ["id", "name"]

df = spark.createDataFrame(data, headers)


df.write.format("iceberg").mode("overwrite").saveAsTable("test_iceberg_table")

spark.sql("describe table extended test_iceberg_table;").show(truncate=False)