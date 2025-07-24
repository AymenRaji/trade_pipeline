{{ config(
    materialized='table'
) }}

WITH stocks AS (
    SELECT
        symbol,
        date,
        open_price,
        close_price,
        daily_return_percentage,
        daily_volume_change
    FROM {{ ref('curated_daily_stock_history') }}
),

news AS (
    SELECT
        symbol,
        date,
        COUNT(*) AS total_articles,
        LISTAGG(headline, ' | ') AS headlines
    FROM {{ ref('curated_daily_news_history') }}
    GROUP BY symbol, date
)

SELECT
    s.*,
    COALESCE(n.total_articles, 0) AS total_articles,
    n.headlines
FROM stocks s
LEFT JOIN news n
    ON s.symbol = n.symbol
   AND s.date = n.date
