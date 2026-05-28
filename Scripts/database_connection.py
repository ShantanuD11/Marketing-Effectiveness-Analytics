from sqlalchemy import create_engine
import pandas as pd
from urllib.parse import quote_plus

username = "root"
password = quote_plus("Doberman2top@")

host = "127.0.0.1"
port = "3306"
database = "consumer_analytics"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

query = "SELECT * FROM train LIMIT 5"

df = pd.read_sql(query, engine)

print(df.head())


query = """
SELECT *
FROM master_sales_data
"""

df = pd.read_sql(query, engine)

print(df.head())
print(df.shape)
print(df.columns)
df['dcoilwtico'] = df['dcoilwtico'].ffill().bfill()

df['transactions'] = df['transactions'].fillna(0)

df['holiday_type'] = df['holiday_type'].fillna('No Holiday')
print(df.isnull().sum())
print(df.info())
df.to_csv('../Exports/master_sales_data.csv', index=False)