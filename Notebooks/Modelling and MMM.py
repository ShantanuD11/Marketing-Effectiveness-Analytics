import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sqlalchemy import create_engine

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import statsmodels.api as sm

import sys
sys.path.append('../scripts')

from data_loader import load_master_data

df = load_master_data()
df['date'] = pd.to_datetime(df['date'])
# Feature Engineering
# FEATURE 1 — Month Feature
df['month'] = df['date'].dt.month
# FEATURE 2 — Day of Week
df['day_of_week'] = df['date'].dt.dayofweek
# FEATURE 3 — Weekend Flag
df['is_weekend'] = np.where(
    df['day_of_week'].isin([5,6]),
    1,
    0
)
# FEATURE 4 — Promotion Flag
df['promo_flag'] = np.where(
    df['onpromotion'] > 0,
    1,
    0
)
# FEATURE 5 — Lag Sales
df = df.sort_values(['store_nbr', 'date'])

df['lag_sales_1'] = (
    df.groupby('store_nbr')['sales']
    .shift(1)
)
# FEATURE 6 — Rolling Average
df['rolling_sales_7'] = (
    df.groupby('store_nbr')['sales']
    .transform(lambda x: x.rolling(7).mean())
)
# FEATURE 7 — Holiday Flag
df['holiday_flag'] = np.where(
    df['holiday_type'].notnull(),
    1,
    0
)

# Handle Missing Values
df = df.dropna()

# Define Modeling Variables
# TARGET VARIABLE
y = df['sales']
# FEATURE VARIABLES
X = df[[
    'onpromotion',
    'transactions',
    'dcoilwtico',
    'month',
    'is_weekend',
    'promo_flag',
    'lag_sales_1',
    'rolling_sales_7',
    'holiday_flag'
]]
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# Build Regression Model
# Add constant
X_train_sm = sm.add_constant(X_train)
X_test_sm = sm.add_constant(X_test)
# Train Model
model = sm.OLS(y_train, X_train_sm).fit()
# View Summary
print(model.summary())
# Prediction
y_pred = model.predict(X_test_sm)
# Model Evaluation
# MAE
mae = mean_absolute_error(y_test, y_pred)
print(mae)
# RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(rmse)
# R square
r2 = r2_score(y_test, y_pred)
print(r2)
# Market MIX Modelling(MMM)
# Contribution Analysis
# Create Coefficient Table
coefficients = pd.DataFrame({
    'Feature': X_train_sm.columns,
    'Coefficient': model.params.values
})
coefficients
# Plot
coefficients.sort_values(
    by='Coefficient',
    ascending=False
).plot(
    x='Feature',
    y='Coefficient',
    kind='bar'
)

plt.title('Feature Contribution Analysis')

plt.show()
# Residual Analysis
residuals = y_test - y_pred

plt.scatter(y_pred, residuals)

plt.axhline(y=0)

plt.title('Residual Analysis')

plt.show()

coefficients = pd.DataFrame({
    'Feature': model.params.index,
    'Coefficient': model.params.values
})
coefficients = coefficients[
    coefficients['Feature'] != 'const'
]
coefficients = coefficients.sort_values(
    by='Coefficient',
    ascending=False
)
coefficients.to_csv(
    '../Exports/mmm_feature_contributions.csv',
    index=False
)