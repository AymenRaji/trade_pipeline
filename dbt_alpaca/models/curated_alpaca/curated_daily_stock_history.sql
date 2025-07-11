{{ config(
    materialized="table"
)}}

with daily_stock as (
    select 
        id,
        symbol,
        date,
        open_price,
        open_volume,
        close_price,
        close_volume,
        close_volume - open_volume AS daily_volume_change
    from DLT_DATA.TRADE_SCHEMA.RAW_DAILY_STOCKS
)


select * from daily_stock