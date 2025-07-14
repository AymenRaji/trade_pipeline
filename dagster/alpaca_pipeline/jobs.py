from dagster import AssetSelection, define_asset_job


Alpaca_ELT_assets = AssetSelection.groups("alpaca_trade") | AssetSelection.groups("dbt_alpaca")
Alpaca_ELT_job = define_asset_job(
    "Alpaca_ELT_jobs",
    selection=Alpaca_ELT_assets.downstream()
)