from abc import ABC, abstractmethod

class Databricks(ABC):
  """Abstract class with static methods that provide core interactivity
  with Databricks and Spark.

  :param spark: Uses the Spark session provided, if not gets or creates new
  :type spark: `spark.sql.SparkSession`, optional
  :param dbutils: Uses the dbutils provided, if not instantiates new
  :type dbutils: `pyspark.dbutils.DBUtils`, optional
  """

  @abstractmethod
  def __init__(self, spark=None, dbutils=None):
    """Constructor method
    """

    self.spark = spark or self.get_spark_session()
    self.dbutils = dbutils or self.get_dbutils(self.spark)


  @staticmethod
  def get_spark_session():
    """Returns a new or found Spark session object
    
    :return: A Spark session object
    :rtype: `spark.sql.SparkSession`
    """
    
    from pyspark.sql import SparkSession
    return SparkSession.builder.getOrCreate()


  @staticmethod
  def get_dbutils(spark=None):
    """Returns a new dbutils object
    
    :param spark: Spark session object, creates new if not provided
    :type spark: `spark.sql.SparkSession`, optional
    :return: A dbutils object
    :rtype: `pyspark.dbutils.DBUtils`
    """
    
    spark = spark or Databricks.get_spark_session()

    try:
      from pyspark.dbutils import DBUtils
      return DBUtils(spark)

    except ImportError:
      from IPython import get_ipython
      return get_ipython().user_ns['dbutils']
