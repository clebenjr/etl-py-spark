from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Exercício PySpark") \
    .config('spark.ui.port', '4050') \
    .getOrCreate()

print('teste')