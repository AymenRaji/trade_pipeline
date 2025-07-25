
from dagster import Definitions, load_assets_from_modules, load_assets_from_package_module
from dagster_embedded_elt.dlt import DagsterDltResource
from dagster_dbt import DbtCliResource


from .assets import alpaca_dbt_assets, alpaca_dlt_asset
from .jobs import Alpaca_ELT_job
from .schedules import Alpaca_ELT_schedule
from .sensors import email_on_filure_sensor

alpaca_dlt_asset = load_assets_from_modules([alpaca_dlt_asset])
alpaca_dbt_asset = load_assets_from_modules([alpaca_dbt_assets])


all_assets = (
    alpaca_dlt_asset
    + alpaca_dbt_asset
)
dlt_resource = DagsterDltResource()
dbt_resource = DbtCliResource(
    project_dir="/opt/dagster/app/dbt",
    profiles_dir="/opt/dagster/app/dbt"
)

defs = Definitions(
    assets=all_assets,
    resources={
        "dlt":dlt_resource,
        "dbt":dbt_resource
    },
    jobs=[Alpaca_ELT_job],
    schedules=[Alpaca_ELT_schedule],
    sensors=[email_on_filure_sensor]
)