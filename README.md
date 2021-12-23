# COVID Data ETL

A repo containing a sample process to extract, transform, and load COVID related data.

## Environment Setup

### **PostgreSQL**

```bash
docker pull postgres
mkdir ~/postgresql-data
docker run -d --name airflow-postgres -p 5432:5432 -v ${HOME}/postgres-data/:/var/lib/postgresql/data -e POSTGRES_PASSWORD=SUPER_SECRET_PASSWORD_HERE postgres
```

### **Airflow**

Follow the instructions [located here](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html) to set up Airflow to run locally.

### **Spark**

Apache Spark should be installed and configured locally to run any Spark related scripts.

## How To Run

## To-Do List
