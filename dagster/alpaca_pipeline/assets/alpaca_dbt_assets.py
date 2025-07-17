from dagster import AssetExecutionContext
from dagster_dbt import DagsterDbtTranslator, DbtCliResource, DbtProject, dbt_assets
from typing import Any, Optional, Mapping
from pathlib import Path


class CustomDagsterDbtTranslator(DagsterDbtTranslator):
    def get_group_name(
            self, dbt_resource_props: Mapping[str, Any]
        ) -> Optional[str]:
            return "dbt_alpaca"

@dbt_assets(
    manifest=Path("dbt/target/", "manifest.json"),
    dagster_dbt_translator=CustomDagsterDbtTranslator()
)
def alpaca_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()