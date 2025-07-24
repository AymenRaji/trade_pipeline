{{ config(
    materialized="view"
) }}

WITH dates AS (
    SELECT
        DATEADD(day, seq4(), '1990-01-01') AS date
    FROM TABLE(GENERATOR(ROWCOUNT => 15000)) -- adjust rowcount to reach 2030
),

filtered_dates AS (
    SELECT
        date
    FROM dates
    WHERE date <= '2030-12-31'
),

dim_date AS (
    SELECT
        date::date as date,
        EXTRACT(day from date) AS day,
        EXTRACT(MONTH FROM date) AS month,
        EXTRACT(YEAR FROM date) AS year,
        EXTRACT(QUARTER FROM date) AS quarter,
        EXTRACT(DOW FROM date) AS day_of_week,
        EXTRACT(WEEK FROM date) AS week,
        CASE
            WHEN EXTRACT(DOW FROM date) IN (0, 6) THEN TRUE
            ELSE FALSE
        END AS is_weekend
    FROM filtered_dates
)

SELECT *
FROM dim_date
