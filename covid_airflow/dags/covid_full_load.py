from datetime import datetime, timedelta
from airflow import DAG
from custom_operators.socrata_operator import SocrataOperator


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

    pull_full_covid_data

if __name__ == "__main__":
    dag.cli()
