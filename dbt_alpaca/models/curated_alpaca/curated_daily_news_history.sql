{{ config(
    materialized="table"
)}}

with source as (
    select
        id,
        created_at,
        updated_at,
        nullif(author, '') as author,
        nullif(content, '')as content,
        nullif(headline, '') as headline,
        nullif(summary, '') as summary,
        nullif(url, '') as news_url,
        nullif(source, '') as news_source,
        symbols
    from {{ source('raw_alpaca', 'raw_daily_news') }}
),

unnested as (
    select
        concat(id,flattened_symbol.value) as id,
        created_at::date as date,
        updated_at,
        author,
        content,
        headline,
        summary,
        news_url,
        news_source,
        flattened_symbol.value::string as symbol
    from source,
    lateral flatten(input => symbols) as flattened_symbol
)

select * 
from unnested
where symbol in ( 'AAPL', 'TSLA', 'AMZN', 'MSFT')
