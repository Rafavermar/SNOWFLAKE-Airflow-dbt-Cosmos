from airflow.operators.dummy_operator import DummyOperator
from astro import sql as aql
from astro.files import File
from astro.sql.table import Table
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
from astronomer.providers.snowflake.utils.snowpark_helpers import SnowparkTable
from pathlib import Path
from airflow.decorators import dag, task
from datetime import datetime
import os
from snowflake.snowpark import Session
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from snowflake.snowpark.functions import max as max_, col





dbt_project_path = Path("/usr/local/airflow/dags/dbt/cosmosproject")
_SNOWFLAKE_CONN_ID = "snowflake_default"

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id=_SNOWFLAKE_CONN_ID,
        profile_args={
            "database": "demo_dbt",
            "schema": "public"
        },
    )
)

snowflake_objects = {
    "demo_database": "DEMO_DBT",
    "demo_schema": "PUBLIC",
}

@dag(default_args={
        "snowflake_conn_id": _SNOWFLAKE_CONN_ID,
    },
    schedule_interval="@daily",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_snowpark",
)


def dbt_snowpark_dag():
    transform_data = DbtTaskGroup(
        group_id="transform_data",
        project_config=ProjectConfig(dbt_project_path),
        profile_config=profile_config,
        execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt"),
        operator_args={"install_deps": True},
    )

    intermediate = DummyOperator(task_id="intermediate")

    snowflake_conn_id2 = "snowflake_default2"

    from airflow.decorators import task
    from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
    from snowflake.snowpark import Session

    @task(task_id="find_best_hotel")
    def find_best_hotel():
        snowflake_conn_id = "snowflake_default2"

        # Utilizar SnowflakeHook para obtener los detalles de conexión seguros
        hook = SnowflakeHook(snowflake_conn_id=snowflake_conn_id)
        conn = hook.get_connection(conn_id=snowflake_conn_id)

        # Crear sesión de Snowpark con los parámetros de conexión seguros
        session = Session.builder.configs({
            "account": "xx00000.eu-west-3.aws",
            "user": conn.login,
            "password": conn.password,
            "warehouse": "DBT_DEV_WH",
            "db": "DEMO_dbt",
            "schema": "ANALYSIS",
            "role": "ACCOUNTADMIN"
        }).create()

        # Obtener el valor máximo de COST en la vista o tabla
        max_cost_df = session.table("DEMO_DBT.ANALYSIS.THIRTY_DAY_AVG_COST").select(max_("COST").alias("max_cost"))
        max_cost = max_cost_df.collect()[0][0]

        # Ahora, filtrar las filas donde COST es igual a ese valor máximo
        highest_cost_hotel_rows = session.table("DEMO_DBT.ANALYSIS.THIRTY_DAY_AVG_COST").filter(
            col("COST") == max_cost).collect()

        if highest_cost_hotel_rows:
            highest_cost_hotel = highest_cost_hotel_rows[0]["HOTEL"]
            print(highest_cost_hotel)
            return highest_cost_hotel
        else:
            print("No data found")
            return "No data found"

    best_hotel = find_best_hotel()
    transform_data >> intermediate >> best_hotel


dag_instance = dbt_snowpark_dag()