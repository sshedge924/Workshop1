from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_workshop.config.ConfigStore import *
from pl_workshop.udfs.UDFs import *

def ds_src_workshop_csv(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("instant", IntegerType(), True), StructField("dteday", DateType(), True), StructField("season", IntegerType(), True), StructField("yr", IntegerType(), True), StructField("mnth", IntegerType(), True), StructField("hr", IntegerType(), True), StructField("holiday", IntegerType(), True), StructField("weekday", IntegerType(), True), StructField("workingday", IntegerType(), True), StructField("weathersit", IntegerType(), True), StructField("temp", DoubleType(), True), StructField("atemp", DoubleType(), True), StructField("hum", DoubleType(), True), StructField("windspeed", DoubleType(), True), StructField("casual", IntegerType(), True), StructField("registered", IntegerType(), True), StructField("cnt", IntegerType(), True)
        ])
        )\
        .option("header", True)\
        .option("inferSchema", True)\
        .option("sep", ",")\
        .csv("dbfs:/databricks-datasets/bikeSharing/data-001/hour.csv")
