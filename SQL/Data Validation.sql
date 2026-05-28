# Row count validation

SELECT COUNT(*) FROM train;
SELECT COUNT(*) FROM stores;
SELECT COUNT(*) FROM transactions;
SELECT COUNT(*) FROM holidays_events;
SELECT COUNT(*) FROM oil;

#  Null values check 
select count(*) as null_values
from train 
where sales is null;

select count(*) as null_values
from train 
where onpromotion is null;

select count(*) as null_values
from train
where store_nbr is null;

select count(*) as null_values
from train
where family is null;

select count(*) as null_values
from train
where date is null;

# Index creation  and  Duplicates check 

CREATE INDEX idx_train_id
ON train(id);

select id, count(*)
from train 
group by id 
having count(*)>1;

# Negative Sales
use consumer_analytics;
select * from train where sales<0;
 
 # Date range validation
 select min(date), max(date) from train;
