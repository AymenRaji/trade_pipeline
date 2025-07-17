import dlt 
from dagster import AssetExecutionContext,  AssetKey, AssetSpec
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets, DagsterDltTranslator
from dagster_dlt.translator import DltResourceTranslatorData
from dlt_pipeline.resource import daily_share_statistics



class CustomDagsterDltTranslator(DagsterDltTranslator):
    def get_asset_spec(self, data: DltResourceTranslatorData) -> AssetSpec:
        """Overrides asset spec to override asset key to be the dlt resource name."""
        default_spec = super().get_asset_spec(data)
        print(data.resource.name)
        return default_spec.replace_attributes(
            key=AssetKey(["raw_alpaca", data.resource.name]),
        )


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
     dagster_dlt_translator=CustomDagsterDltTranslator(),
)



def alpaca_dlt_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)