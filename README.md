# FMCG Marketing Effectiveness & Sales Analytics Project

## Project Overview

This project is an end-to-end business analytics solution developed for analyzing retail sales performance, marketing effectiveness, customer behavior, and sales forecasting within an FMCG (Fast-Moving Consumer Goods) retail environment.

The project combines SQL, Python, statistical modeling, forecasting, and Power BI to generate actionable business insights and support data-driven decision-making.

The objective of the project is to understand:

* What drives sales performance
* How promotions impact revenue
* Which regions and product categories perform best
* How customer transactions influence sales
* How seasonality affects demand
* How future sales can be forecasted

---

# Business Problem

Retail and FMCG businesses generate massive amounts of transactional data daily. However, deriving meaningful business insights from this data requires structured analytics workflows and statistical modeling.

This project focuses on solving key business problems such as:

* Measuring promotional effectiveness
* Identifying sales drivers
* Forecasting future demand
* Improving inventory planning
* Understanding customer purchasing behavior
* Supporting marketing optimization

---

# Tech Stack

## Database & SQL

* MySQL

## Programming & Analytics

* Python
* pandas
* NumPy
* statsmodels
* scikit-learn

## Visualization

* Power BI
* matplotlib
* seaborn

## Forecasting & Modeling

* Regression Modeling
* Marketing Mix Modeling (MMM)
* ARIMA Forecasting

---

# Project Architecture

```text
MySQL → Data Cleaning → Feature Engineering → Python EDA → Statistical Modeling → Forecasting → Power BI Dashboard
```

---

# Project Workflow

## 1. Data Ingestion & SQL Processing

* Imported retail sales datasets into MySQL
* Created relational tables and schema
* Performed data validation and cleaning
* Built SQL-based KPI calculations
* Created master analytical dataset

## 2. Exploratory Data Analysis (EDA)

* Analyzed sales trends and seasonality
* Studied product category performance
* Evaluated regional sales distribution
* Identified promotional impact on sales
* Performed correlation and outlier analysis

## 3. Statistical Modeling & Marketing Mix Modeling (MMM)

* Built regression-based sales prediction model
* Evaluated contribution of promotions to revenue
* Analyzed customer transaction impact
* Studied historical sales influence on future demand
* Performed residual and coefficient analysis

## 4. Forecasting

* Developed ARIMA-based forecasting model
* Predicted future sales trends
* Evaluated forecasting accuracy
* Generated business planning insights

## 5. Dashboard & Reporting

* Built interactive Power BI dashboards
* Created executive-level business visualizations
* Developed KPI reporting and forecasting dashboards
* Generated strategic business recommendations

---

# Key Business Insights

* Promotional activity significantly increases sales performance.
* Customer transactions positively influence revenue generation.
* Historical sales trends strongly impact future demand.
* Seasonal demand fluctuations exist across the business.
* Regional sales performance varies significantly across locations.
* Forecasting can support inventory and operational planning.

---

# Dashboard Overview

The Power BI dashboard includes:

## Executive Business Overview

* Total Revenue
* Total Transactions
* Sales Trends
* Product Category Performance
* Regional Revenue Analysis

## Marketing Effectiveness & Forecasting

* Promotion Impact Analysis
* Promotional Contribution to Sales
* Forecasted Future Sales
* Key Sales Drivers Analysis

---

# Project Structure

```text
FMCG-Marketing-Effectiveness-Analytics/
│
├── data/
├── sql/
├── notebooks/
├── scripts/
├── exports/
├── dashboard/
├── reports/
├── presentation/
├── images/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# SQL Workflow

The SQL layer of the project includes:

* Schema creation
* Data validation
* Data cleaning
* KPI calculations
* Feature engineering
* Master table creation

SQL scripts are organized sequentially inside the `sql/` directory.

---

# Statistical Modeling

The project uses regression-based statistical modeling techniques to estimate the impact of multiple business drivers on sales performance.

Key modeling variables include:

* Promotions
* Transactions
* Historical Sales
* Seasonal Variables
* Holiday Effects
* Economic Indicators

The project also includes Marketing Mix Modeling (MMM) concepts for analyzing promotional effectiveness.

---

# Forecasting

ARIMA-based forecasting models were developed to:

* predict future sales demand,
* support inventory planning,
* and improve business decision-making.

Forecasting outputs were integrated into the Power BI dashboard for executive visualization.

---

# Business Recommendations

Based on the analysis, the project recommends:

* Optimizing promotional campaign timing
* Improving forecast-driven inventory planning
* Increasing marketing investment during peak demand periods
* Prioritizing high-performing regions
* Expanding analytics using external business variables

---

# Future Improvements

Future enhancements may include:

* Advanced machine learning models
* Automated ETL pipelines
* Cloud-based deployment
* Real-time dashboard integration
* Advanced time-series forecasting models
* Additional external business data integration

---

# Skills Demonstrated

## Technical Skills

* MySQL
* Python
* Data Cleaning
* SQL Analytics
* Exploratory Data Analysis
* Regression Modeling
* Forecasting
* Power BI

## Business & Analytical Skills

* Marketing Effectiveness Analysis
* KPI Development
* Business Storytelling
* Forecast-Driven Decision Making
* Data-Driven Recommendations

---

# Conclusion

This project demonstrates a complete end-to-end business analytics workflow for FMCG retail sales analysis and marketing effectiveness evaluation.

The project combines data engineering, statistical modeling, forecasting, visualization, and business storytelling to generate actionable insights and support strategic business decision-making.
