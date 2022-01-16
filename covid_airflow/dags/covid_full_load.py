from datetime import datetime, timedelta
from airflow import DAG
from custom_operators.socrata_operator import SocrataOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

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

    pull_full_covid_data >> trunc_staging_table

if __name__ == "__main__":
    dag.cli()
