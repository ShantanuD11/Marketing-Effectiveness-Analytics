import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sqlalchemy import create_engine

from sklearn.metrics import mean_absolute_error, mean_squared_error

from statsmodels.tsa.arima.model import ARIMA
import sys
sys.path.append('../scripts')

from data_loader import load_master_data

df = load_master_data()
df['date'] = pd.to_datetime(df['date'])
# Prepare Time-Series Dataset
# Aggregate Daily Sales
daily_sales = (
    df.groupby('date')['sales']
    .sum()
    .reset_index()
)
# Set Date as Index
daily_sales.set_index('date', inplace=True)
daily_sales = daily_sales.asfreq('D')
daily_sales.isnull().sum()
# Plot Sales Trend
plt.figure(figsize=(15,6))

plt.plot(daily_sales.index, daily_sales['sales'])

plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')

plt.show()
# Train-Test Split for Forecasting
# Split Data
train = daily_sales.iloc[:-30]
test = daily_sales.iloc[-30:]
# Build ARIMA Forecasting Model
# Create Model
model = ARIMA(
    train['sales'],
    order=(5,1,0)
)
# Train Model
model_fit = model.fit()
# Generate Forecast
forecast = model_fit.forecast(steps=30)
# Visualize Forecast
# Plot
plt.figure(figsize=(15,6))

plt.plot(train.index, train['sales'], label='Train')

plt.plot(test.index, test['sales'], label='Actual')

plt.plot(test.index, forecast, label='Forecast')

plt.legend()

plt.title('Sales Forecasting')

plt.show()
# Forecast Evaluation
# MAE
mae = mean_absolute_error(
    test['sales'],
    forecast
)

print(mae)
# RMSE
rmse = np.sqrt(
    mean_squared_error(
        test['sales'],
        forecast
    )
)

print(rmse)
# Forecast Future Sales
# Retrain Full Model
final_model = ARIMA(
    daily_sales['sales'],
    order=(5,1,0)
)

final_model_fit = final_model.fit()
# Predict Next 60 Days
future_forecast = final_model_fit.forecast(steps=60)
# Create Future Dates
future_dates = pd.date_range(
    start=daily_sales.index[-1],
    periods=60,
    freq='D'
)
# Forecast DataFrame
forecast_df = pd.DataFrame({
    'date': future_dates,
    'forecast_sales': future_forecast
})
# Plot Future Forecast
plt.figure(figsize=(15,6))

plt.plot(
    daily_sales.index,
    daily_sales['sales'],
    label='Historical Sales'
)

plt.plot(
    forecast_df['date'],
    forecast_df['forecast_sales'],
    label='Future Forecast'
)

plt.legend()

plt.title('Future Sales Forecast')

plt.show()
# Advanced Business Analytics- Recommendations Documentation
# Export Forecast Results
# Export CSV
forecast_df.to_csv(
    '../exports/future_sales_forecast.csv',
    index=False
)

historical = daily_sales.reset_index()

historical['type'] = 'Historical'

historical.rename(
    columns={'sales':'value'},
    inplace=True
)
forecast_final = forecast_df.copy()

forecast_final['type'] = 'Forecast'

forecast_final.rename(
    columns={'forecast_sales':'value'},
    inplace=True
)
historical = historical[['date', 'value', 'type']]

forecast_final = forecast_final[['date', 'value', 'type']]

combined_forecast = pd.concat(
    [historical, forecast_final]
)

combined_forecast.to_csv(
    '../exports/combined_forecast.csv',
    index=False
)