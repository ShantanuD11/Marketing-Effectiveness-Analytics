# Standardize Categories
SET SQL_SAFE_UPDATES = 0;
UPDATE stores
SET city = UPPER(city);
SET SQL_SAFE_UPDATES = 1;

# Create Clean Views
CREATE VIEW clean_sales AS
SELECT *
FROM train
WHERE sales >= 0;