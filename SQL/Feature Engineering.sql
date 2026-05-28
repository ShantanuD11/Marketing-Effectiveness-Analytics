# Aggregated Daily Sales
CREATE VIEW daily_store_sales AS
SELECT
    date,
    store_nbr,
    SUM(sales) AS total_sales,
    SUM(onpromotion) AS total_promotions
FROM train
GROUP BY date, store_nbr;

# Rolling Average
SELECT
    date,
    store_nbr,
    total_sales,
    AVG(total_sales) OVER(
        PARTITION BY store_nbr
        ORDER BY date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7day_avg
FROM daily_store_sales;

# Lag Features
SELECT
    date,
    store_nbr,
    total_sales,
    LAG(total_sales,1) OVER(
        PARTITION BY store_nbr
        ORDER BY date
    ) AS prev_day_sales
FROM daily_store_sales;

# Month Feature
SELECT *,
       MONTH(date) AS month_num
FROM train;

# Weekend Feature
SELECT *,
       CASE
           WHEN DAYOFWEEK(date) IN (1,7)
           THEN 1
           ELSE 0
       END AS is_weekend
FROM train;

