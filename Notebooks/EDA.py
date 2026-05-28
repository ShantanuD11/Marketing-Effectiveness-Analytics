import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sqlalchemy import create_engine

import sys
sys.path.append('../scripts')

from data_loader import load_master_data

df = load_master_data()

# 1.  SALES TREND ANALYSIS BUSINESS QUESTION
# “How are sales behaving over time?”
# Convert Date
df['date'] = pd.to_datetime(df['date'])
# Daily Sales Trend
daily_sales = df.groupby('date')['sales'].sum().reset_index()
# Plot Trend
plt.figure(figsize=(15,6))
plt.plot(daily_sales['date'], daily_sales['sales'])

plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')

plt.show()
# PRODUCT FAMILY ANALYSIS
# BUSINESS QUESTION
# “Which product categories drive revenue?”
# Aggregate
family_sales = (
    df.groupby('family')['sales']
    .sum()
    .sort_values(ascending=False)
)
# Plot trend
plt.figure(figsize=(12,6))

family_sales.head(10).plot(kind='bar')

plt.title('Top Product Families by Sales')
plt.ylabel('Revenue')

plt.show()
# PROMOTION EFFECTIVENESS ANALYSIS BUSINESS QUESTION
# “Do promotions actually increase sales?”
# Create Promotion Flag
df['promo_flag'] = np.where(df['onpromotion'] > 0, 1, 0)
# Compare Sales
promo_analysis = (
    df.groupby('promo_flag')['sales']
    .mean()
)
# Plot trend
promo_analysis.plot(kind='bar')

plt.title('Average Sales: Promotion vs No Promotion')
plt.ylabel('Average Sales')

plt.show()
# SEASONALITY ANALYSIS BUSINESS QUESTION
# “Do certain months perform better?”
#Create Month Feature
df['month'] = df['date'].dt.month
# Aggregate
monthly_sales = (
    df.groupby('month')['sales']
    .sum()
)
# Plot
monthly_sales.plot(kind='line', marker='o')

plt.title('Monthly Sales Trend')

plt.show()
# STORE / REGIONAL ANALYSIS BUSINESS QUESTION
# “Which regions perform best?”
# Aggregate
city_sales = (
    df.groupby('city')['sales']
    .sum()
    .sort_values(ascending=False)
)
# Plot
city_sales.head(10).plot(kind='bar')

plt.title('Top Cities by Revenue')

plt.show()
# HOLIDAY IMPACT ANALYSIS BUSINESS QUESTION
# “Do holidays affect sales?”
# Aggregate
holiday_sales = (
    df.groupby('holiday_type')['sales']
    .mean()
)
# Plot
holiday_sales.plot(kind='bar')

plt.title('Average Sales by Holiday Type')

plt.show()

# TRANSACTION VS SALES ANALYSIS BUSINESS QUESTION
# “Does higher footfall increase sales?”
# Scatter Plot
plt.figure(figsize=(8,6))

plt.scatter(
    df['transactions'],
    df['sales'],
    alpha=0.3
)

plt.xlabel('Transactions')
plt.ylabel('Sales')

plt.title('Transactions vs Sales')

plt.show()

# CORRELATION ANALYSIS
# Select Numeric Variables
numeric_df = df.select_dtypes(include=np.number)
# Correlation Matrix
corr = numeric_df.corr()
# Heatmap
plt.figure(figsize=(10,8))

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Matrix')

plt.show()

# OUTLIER ANALYSIS
# Boxplot
plt.figure(figsize=(10,6))

sns.boxplot(x=df['sales'])

plt.title('Sales Distribution')

plt.show()
