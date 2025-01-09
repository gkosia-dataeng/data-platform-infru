from delta.tables import DeltaTable
from pyspark.sql import SparkSession

def main():

    spark = SparkSession.builder \
        .appName("Test delt job") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.sql.catalogImplementation", "hive") \
        .config("spark.sql.warehouse.dir", "s3a://lakehouse/warehouse/delta") \
        .config("spark.jars", "/opt/bitnami/spark/jars/delta-core_2.12-2.4.0.jar,/opt/bitnami/spark/jars/delta-storage-2.4.0.jar") \
        .enableHiveSupport() \
        .getOrCreate()

    spark.sql("DROP SCHEMA IF EXISTS bronze CASCADE")

    spark.sql("CREATE DATABASE IF NOT EXISTS bronze")
    spark.sql("USE bronze")

    data = [(1, "aa"), (2, "bb")]
    headers = ["id", "name"]

    df = spark.createDataFrame(data, headers)

    df.show()

    (
        df.
        write.
        format("delta").
        option("delta.columnMapping.mode", "name").
        saveAsTable("test_table")
    )

    dt = DeltaTable.forName(spark, "bronze.test_table")

    dt.toDF().show()


if __name__ == "__main__":
    main()