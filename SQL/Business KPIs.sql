# Business KPI's

# Total Revenue
SELECT ROUND(SUM(sales),2) AS total_sales
FROM train;

# Sales by Category
SELECT family,
       ROUND(SUM(sales),2) AS revenue
FROM train
GROUP BY family
ORDER BY revenue DESC;

# Promotion Impact
SELECT
    CASE
        WHEN onpromotion > 0 THEN 'Promotion'
        ELSE 'No Promotion'
    END AS promo_flag,
    ROUND(AVG(sales),2) AS avg_sales
FROM train
GROUP BY promo_flag;

# Regional Sales
SELECT s.city,
       ROUND(SUM(t.sales),2) AS total_sales
FROM train t
JOIN stores s
ON t.store_nbr = s.store_nbr
GROUP BY s.city
ORDER BY total_sales DESC;

# Monthly Trends
SELECT MONTH(date) AS month_num,
       ROUND(SUM(sales),2) AS monthly_sales
FROM train
GROUP BY month_num
ORDER BY month_num;

# Holiday Impact
SELECT h.type,
       ROUND(AVG(t.sales),2) AS avg_sales
FROM train t
JOIN holidays_events h
ON t.date = h.date
GROUP BY h.type;

