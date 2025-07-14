import dlt 
from dagster import AssetExecutionContext
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from dlt_pipeline.resource import daily_share_statistics




# Define dlt source
@dlt_assets(
    dlt_source=daily_share_statistics(),
    dlt_pipeline=dlt.pipeline(
        pipeline_name="trade",
        destination='snowflake',
        dataset_name="raw_alpaca",
        progress="log"
    ),
    name="alpaca_trade_shares",
    group_name="alpaca_trade",
)



def alpaca_dlt_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)