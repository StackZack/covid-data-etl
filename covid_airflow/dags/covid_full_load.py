import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.models.variable import Variable
from socrata_provider.operators.socrata import SocrataOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.apache.spark.operators.spark_submit import (
    SparkSubmitOperator
)

JDBC_HOME = Variable.get("JDBC_HOME")
JDBC_POSTGRES = Variable.get("JDBC_POSTGRES")
PYSPARK_HOME = Variable.get("PYSPARK_HOME")

with DAG(
    dag_id="covid_full_load",
    description="Executes ETL for full load of COVID data.",
    schedule_interval="@daily",
    start_date=datetime(2022, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=10),
    tags=["covid", "etl", "full"]
) as dag:
    pull_full_covid_data = SocrataOperator(
        task_id="pull_full_covid_data",
        data_id="9bhg-hcku",
        file_dir="/tmp"
    )

    trunc_staging_table = PostgresOperator(
        task_id="trunc_staging_table",
        sql="""
        TRUNCATE stg_full_covid;
        """
    )

    clean_covid_data = SparkSubmitOperator(
        task_id="clean_covid_data",
        application=os.path.join(PYSPARK_HOME, "clean_covid_data.py"),
        application_args=[
            "{{ ti.xcom_pull(task_ids='pull_full_covid_data') }}"
        ]
    )

    pull_full_covid_data >> trunc_staging_table >> clean_covid_data

if __name__ == "__main__":
    dag.cli()
