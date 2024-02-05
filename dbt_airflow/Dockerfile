# syntax=quay.io/astronomer/airflow-extensions:latest

FROM quay.io/astronomer/astro-runtime:10.3.0-python-3.9-base

COPY ./astro_provider_snowflake-0.0.0-py3-none-any.whl /tmp/

# Create the virtual environment
PYENV 3.8 snowpark requirements-snowpark.txt

# Install packages into the virtual environment
COPY requirements-snowpark.txt /tmp
RUN python3.8 -m pip install -r /tmp/requirements-snowpark.txt
COPY requirements.txt /tmp
RUN python3.8 -m pip install -r /tmp/requirements.txt

RUN python3.8 -m venv dbt_venv && . dbt_venv/bin/activate && pip install --no-cache-dir dbt-snowflake && pip install --no-cache-dir snowflake-connector-python==3.7.0 && pip install --no-cache-dir dbt-postgres && deactivate