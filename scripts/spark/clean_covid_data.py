import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, StructType

FILE_PATH = "/tmp"
FILE_NAME = "cleaned_covid_data.csv"

# Create spark session
spark = (
    SparkSession
    .builder
    .appName("clean_covid_data")
    .getOrCreate()
)

# Define schema
schema = StructType([
    StructField("csv_row", StringType(), False),
    StructField("data_as_of", StringType(), False),
    StructField("start_date", StringType(), False),
    StructField("end_date", StringType(), False),
    StructField("data_group", StringType(), False),
    StructField("us_state", StringType(), False),
    StructField("sex", StringType(), False),
    StructField("age_group", StringType(), False),
    StructField("covid_19_deaths", StringType(), True),
    StructField("total_deaths", StringType(), True),
    StructField("pneumonia_deaths", StringType(), True),
    StructField("pneumonia_and_covid_19_deaths", StringType(), True),
    StructField("influenza_deaths", StringType(), True),
    StructField("pneumonia_influenza_or_covid", StringType(), True),
    StructField("footnote", StringType(), True),
    StructField("case_year", StringType(), True),
    StructField("case_month", StringType(), True)
])

# Read CSV file into dataframe
df = (
    spark.read.format("csv")
    .schema(schema)
    .option("header", "true")
    .load(sys.argv[1])
)

# Write cleaned data frame to CSV file
df.repartition(1).write.format("csv").mode("overwrite").save(
    os.path.join(FILE_PATH, FILE_NAME)
)
