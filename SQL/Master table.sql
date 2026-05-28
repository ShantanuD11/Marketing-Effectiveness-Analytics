CREATE VIEW master_sales_data AS
SELECT
    t.date,
    t.store_nbr,
    s.city,
    s.state,
    s.type,
    s.cluster,
    t.family,
    t.sales,
    t.onpromotion,
    tr.transactions,
    o.dcoilwtico,
    h.type AS holiday_type
FROM train t
LEFT JOIN stores s
    ON t.store_nbr = s.store_nbr
LEFT JOIN transactions tr
    ON t.date = tr.date
    AND t.store_nbr = tr.store_nbr
LEFT JOIN oil o
    ON t.date = o.date
LEFT JOIN holidays_events h
    ON t.date = h.date;