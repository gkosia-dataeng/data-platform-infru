from delta.tables import DeltaTable
from pyspark.sql import SparkSession

def main():

    spark = SparkSession.builder \
        .appName("Test cluster job") \
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