# COVID Data ETL

A repo containing a sample process to extract, transform, and load COVID related data.

## Environment Setup

### **Spark**

Apache Spark should be installed and configured locally to run Spark related scripts.

### **PostgreSQL**

#### **Tools**

```bash
brew install postgresql  # needed for running postgresql operators
docker pull postgres  # pull image for running docker in container
mkdir ~/postgresql-data  # make directory for persistent db storage
docker run -d --name airflow-postgres -p 5432:5432 \
-v ${HOME}/postgres-data/:/var/lib/postgresql/data \
-e POSTGRES_PASSWORD=SUPER_SECRET_PASSWORD_HERE postgres
```

#### **Tables**

Run the code within **sql/schema.sql** in your local Postgres database to create the required tables.

### **Apache Airflow**

Follow the instructions [located here](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html) to set up Airflow to run locally.

#### **Variables in Airflow**

Add the below variables to your Apache Airflow instance for use in the custom dag.

|Key            |Val                        |
|---------------|---------------------------|
|PYSPARK_HOME   |airflow/scripts/pyspark    |
|JDBC_HOME      |airflow/jars/jdbc          |
|JDBC_POSTGRES  |YOUR_POSTGRES_JAR_NAME     |

#### **Socrata Connection in Airflow**

Create a new connection in your Apache Airflow instance with the below values.

|Metadata ID    |Value              |
|---------------|-------------------|
|Connection Id  |http_socrata       |
|Connection Type|HTTP               |
|Host           |data.cdc.gov       |
|Login          |LOGIN_EMAIL_HERE   |
|Extra          |APP_TOKEN_HERE     |

The **APP_TOKEN_HERE** should be formatted like the below example

```javascript
{
    "app_token": "VALUE_OF_TOKEN"
}
```

#### **Postgres Connection in Airflow**

Update metadata of the _**postgres_default**_ Apache Airflow connection to point to local postgres instance. Assuming you used the PostgreSQL docker commands in this README, reference the below table for the appropriate values.

|Metadata ID    |Value              |
|---------------|-------------------|
|Connection Id  |postgres_default   |
|Connection Type|Postgres           |
|Host           |localhost          |
|Schema         |postgres           |
|Login          |postgres           |
|Password       |PASSWORD_HERE      |
|Port           |5432               |

#### **Spark Standalone Connection in Airflow**

Update metadata of the _**spark_default**_ Apache Airflow connection to point to local spark instance. The below values are based on a local standalone instance with the default ports in place.

|Metadata ID    |Value              |
|---------------|-------------------|
|Connection Id  |spark_default      |
|Connection Type|Spark              |
|Host           |spark://localhost  |
|Port           |7077               |

#### **Spark JDBC Connection in Airflow**

Create a new connection in your Apache Airflow instance with the below values. This assumes you used the PostgreSQL docker commands in this README.

|Metadata ID    |Value              |
|---------------|-------------------|
|Connection Id  |jdbc_default       |
|Connection Type|Spark JDBC         |
|Host           |localhost          |
|Schema         |postgres           |
|Login          |postgres           |
|Password       |PASSWORD_HERE      |
|Port           |5432               |

## How To Run

## To-Do List
1. Update clean_covid_data spark script to split data and clean data as needed.
2. Update SQL schema to split into a better data model.
3. Add spark script(s) to load data into respective tables.
4. Refactor Socrata operator accept optional connection parameter.
5. Start dockerizing entire environment for ease of use.