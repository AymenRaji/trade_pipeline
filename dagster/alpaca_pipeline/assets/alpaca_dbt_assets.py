from dagster import AssetExecutionContext
from dagster_dbt import DagsterDbtTranslator, DbtCliResource, DbtProject, dbt_assets
from typing import Any, Optional, Mapping
from pathlib import Path


class CustomDagsterDbtTranslator(DagsterDbtTranslator):
    def __init__(self, group_name: str):
        self.group_name = group_name

    def get_group_name(self, dbt_resource_props: Mapping[str, Any]) -> Optional[str]:
        return self.group_name

@dbt_assets(
    manifest=Path("dbt/target/", "manifest.json"),
    dagster_dbt_translator=CustomDagsterDbtTranslator("dbt_alpaca"),
    select="tag:alpaca"
)
def alpaca_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()