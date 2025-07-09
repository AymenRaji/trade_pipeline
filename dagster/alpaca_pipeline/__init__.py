
from dagster import Definitions, load_assets_from_modules, load_assets_from_package_module
from dagster_embedded_elt.dlt import DagsterDltResource


from .assets import alpaca_dlt_asset
from .jobs import Alpaca_ELT_job
from .schedules import Alpaca_ELT_schedule

alpaca_dlt_asset = load_assets_from_modules([alpaca_dlt_asset])

all_assets = (
    alpaca_dlt_asset
)
dlt_resource = DagsterDltResource()

defs = Definitions(
    assets=all_assets,
    resources={
        "dlt":dlt_resource
    },
    jobs=[Alpaca_ELT_job],
    schedules=[Alpaca_ELT_schedule]
)