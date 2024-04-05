from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_workshop.config.ConfigStore import *
from pl_workshop.udfs.UDFs import *
from prophecy.utils import *
from pl_workshop.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_src_workshop_csv = ds_src_workshop_csv(spark)
    ds_tgt_ws_csv(spark, df_ds_src_workshop_csv)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_Workshop")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_Workshop")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_Workshop", config = Config)(pipeline)

if __name__ == "__main__":
    main()
