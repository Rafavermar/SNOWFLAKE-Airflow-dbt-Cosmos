from datetime import datetime
import os
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
from pathlib import Path

dbt_project_path = Path("/usr/local/airflow/dags/dbt/cosmosproject")

profile_config = ProfileConfig(profile_name="default",
                               target_name="dev",
                               profile_mapping=SnowflakeUserPasswordProfileMapping(conn_id="cosmosDag",
                                                                                   profile_args={
                                                                                       "database": "demo_dbt",
                                                                                       "schema": "public"
                                                                                   },
                                                                                   ))

dbt_snowflake_dag = DbtDag(project_config=ProjectConfig(dbt_project_path, ),
                           operator_args={"install_deps": True},
                           profile_config=profile_config,
                           execution_config=ExecutionConfig(
                               dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt", ),
                           schedule_interval="@daily",
                           start_date=datetime(2023, 9, 10),
                           catchup=False,
                           dag_id="dbt_snowflake_dag")
