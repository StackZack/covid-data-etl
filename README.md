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
|Port           |5432               |

## How To Run
