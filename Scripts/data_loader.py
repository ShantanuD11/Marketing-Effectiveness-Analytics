import pandas as pd
from database_connection import engine


def load_master_data():

    query = """
    SELECT *
    FROM master_sales_data
    """

    df = pd.read_sql(query, engine)

    return df