# SnowflakeAirflowDbtCosmos Project
![snowflake_architecture.png](assets%2Fsnowflake_architecture.png)
## Overview

Welcome to the SnowflakeAirflowDbtCosmo project, a demonstration of integrating Airflow, DBT, and Snowflake with Snowpark for advanced data analysis. This project, generated with `astro dev init` using the Astronomer CLI, showcases how to run Apache Airflow locally, building both simple and advanced data pipelines involving Snowflake.

### What You'll Build

- A simple Airflow pipeline leveraging DBT and Snowflake for data transformation.
- A more complex pipeline using Snowpark for data analysis with Python.

## Prerequisites

- **Snowflake Account** with a user having permissions to create objects in `DEMO_DB`.
- **Snowpark Enabled** on your Snowflake environment.
- **GitHub Account** for version control. [Sign up for GitHub](https://github.com/join) if needed.
- **Docker Desktop** installed to run Airflow in containers. [Download Docker](https://www.docker.com/products/docker-desktop).
- **Astro CLI** version 1.22.0 installed for Airflow environment management. Follow the [Astro CLI setup instructions](https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart).

## Project Contents
- `assets`: Contains additional informations like SQL queries, screenshots and bookmarks where I founded almost all the information
- `dags/`: Contains your Airflow DAGs, including example DAGs for basic and advanced use cases.
- `Dockerfile`: Specifies a versioned Astro Runtime Docker image for Airflow.
- `include/`, `packages.txt`, `requirements.txt`, `plugins/`: Directories for additional project files, OS-level packages, Python packages, and custom plugins.
- `airflow_settings.yaml`: Specifies Airflow Connections, Variables, and Pools for local development.

## Deploy Your Project Locally

1. **Start Airflow**: Run `astro dev start` to spin up Docker containers for Airflow components (Postgres, Webserver, Scheduler, Triggerer).
2. **Verify Containers**: Ensure all Docker containers are up by running `docker ps`.
3. **Access Airflow UI**: Visit http://localhost:8080/ (default login: `admin`/`admin`) and configure connections as described in the provided article for Snowflake communication.

## Deploy Your Project to Astronomer

For deploying to Astronomer, refer to the [official documentation](https://docs.astronomer.io/cloud/deploy-code/).

## Next Steps

After configuring Airflow connections, execute the DAGs and monitor their progress. Review the `findbesthotel` task logs for results.

## Further information

Under assets folder, you can find useful informacion such us websites, SQL commnands needed and orientation for the parameters by initializing dbt.
This project is based on the official quick start from Snowflake. However I must to update, change code and find missing operators in order to accomplish the whole project.

check my article here: [Data Engineering with Apache Airflow, Snowflake, Snowpark, dbt & Cosmos, Astronomer](https://www.linkedin.com/pulse/data-engineering-apache-airflow-snowflake-snowpark-dbt-vera-mara%C3%B1%C3%B3n-f9ese/)

check the quick start tutorial here:
[Quick start Official Snowflake](https://docs.astronomer.io/cloud/deploy-code/](https://quickstarts.snowflake.com/guide/data_engineering_with_apache_airflow/index.html?index=..%2F..index#0)https://quickstarts.snowflake.com/guide/data_engineering_with_apache_airflow/index.html?index=..%2F..index#0). 

## Note

This project does not implement Streamlit.

