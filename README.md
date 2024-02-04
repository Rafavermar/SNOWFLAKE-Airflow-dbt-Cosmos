# SnowflakeAirflowDbtCosmos Project

## Overview

This project demonstrates the integration of Airflow, DBT, and Snowflake, utilizing Snowpark to enable advanced data analysis. You will build a simple Airflow pipeline that leverages DBT and Snowflake for data transformation and a more complex pipeline incorporating Snowpark for data analysis with Python.

## Prerequisites

- **Snowflake Account**: Ensure you have access to a Snowflake account.
- **Snowflake User**: Create a user with permissions to create objects in the `DEMO_dbt` database.
- **Snowpark Enabled**: Verify Snowpark is enabled in your Snowflake environment.
- **GitHub Account**: Needed for version control. [Join GitHub](https://github.com/join) if you don't have an account.
- **Docker Desktop**: Install Docker Desktop to run Airflow in containers. [Download Docker](https://www.docker.com/products/docker-desktop).
- **Astro CLI**: Install Astro CLI version 1.22.0 for managing Airflow environments. Follow the [Astro CLI setup instructions](https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart).

## Setup Instructions

1. **Prepare Snowflake**: Ensure you have a warehouse, database, and tables set up in Snowflake.
2. **Clone Repository**: Clone this repository to your local machine.
3. **Start Environment**: Navigate to the project directory (`\path\to\SnowflakeAirflowDbtCosmo\dbt_airflow`) and run `astro dev start` to launch Docker with Postgres and Airflow.
4. **Access Airflow UI**: Open a browser and navigate to `localhost:8080` to view the Airflow UI.
5. **Configure Airflow Connections**: Follow the steps in the provided article to set up three necessary connections in Airflow for communication with Snowflake.

## Building the Pipeline

- You will build a basic Airflow pipeline that uses DBT and Snowflake for data processing.
- Additionally, you will create a more advanced pipeline that incorporates Snowpark for data analysis with Python.

## Note

Streamlit has not been implemented in this project.

## Next Steps

After setting up the connections in Airflow, trigger the DAGs and monitor their execution. Upon successful completion, review the logs of the `findbesthotel` task in Airflow to see the results.

This guide outlines the steps to quickly deploy and run the project, enabling data transformation and analysis workflows using Airflow, DBT, and Snowflake.
