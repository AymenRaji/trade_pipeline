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
        round(DIV0(close_price - open_price, open_price) * 100, 2) AS daily_return_perecntage,
        close_volume - open_volume AS daily_volume_change
    from {{ source('raw_alpaca', 'raw_daily_stocks')}}
)


select * from daily_stock