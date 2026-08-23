# Apple Stock Price Analysis & ML Prediction 🍏📈

This project performs statistical analysis, correlation visualization, and uses a Machine Learning model (Linear Regression) to predict the daily returns of Apple (AAPL) stock. 

## 📋 Overview

The script fetches the last 3 years of Apple's stock data using Yahoo Finance. It then conducts exploratory data analysis (EDA) to understand the stock's behavior, calculates daily returns and volatility, and finally trains a Linear Regression model to predict future daily returns based on specific stock features.

## ✨ Features

* **Data Extraction:** Automatically downloads historical daily stock data for Apple (AAPL) using the `yfinance` library.
* **Statistical Analysis:** Calculates descriptive statistics, including the mean and standard deviation of the closing price.
* **Data Visualization:** 
  * Line plot of Daily Returns over time.
  * Heatmap of the Correlation Matrix using Seaborn.
  * Scatter plot comparing Actual vs. Predicted returns.
* **Feature Engineering:** Calculates daily `Volatility` (High - Low) and `Returns` (percentage change in Close price).
* **Machine Learning:** Uses `scikit-learn`'s Linear Regression model to predict stock returns based on Volume, Close Price, and Volatility, and evaluates the model using the $R^2$ score.

## 🛠️ Prerequisites

To run this code, you will need Python installed along with the following libraries:

```bash
pip install yfinance numpy pandas matplotlib seaborn scipy scikit-learn
