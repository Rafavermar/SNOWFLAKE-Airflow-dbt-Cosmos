# SnowflakeAirflowDbtCosmos Project

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

## Contact

For support with the Astronomer CLI or any deployment issues, please reach out to Astronomer support.

## Note

This project does not implement Streamlit.

