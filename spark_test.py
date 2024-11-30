from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("SparkTest").getOrCreate()
print("Spark session created successfully!")
