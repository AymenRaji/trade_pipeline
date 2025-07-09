from dagster import ScheduleDefinition
from .jobs import Alpaca_ELT_job

Alpaca_ELT_schedule = ScheduleDefinition(
    job = Alpaca_ELT_job,
    execution_timezone="America/Toronto",
    cron_schedule="05 13 * * *"
)