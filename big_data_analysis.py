from pyspark.sql import SparkSession

def count_rows(file_path):
    spark = SparkSession.builder.appName("BigDataAnalysis").getOrCreate()
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    row_count = df.count()
    spark.stop()
    return row_count

if __name__ == "__main__":
    file_path = 'big_data_sample.csv'
    total_rows = count_rows(file_path)
    print(f"The total number of rows in the dataset is: {total_rows}")
