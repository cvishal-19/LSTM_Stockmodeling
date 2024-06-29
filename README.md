## Overview

This project utilizes an LSTM (Long Short-Term Memory) model to predict stock prices based on historical data. The model incorporates technical indicators like RSI, CCI, VWAP, and ROC to generate trading signals, which are used to train and evaluate the LSTM.

1. **Data Loading and Preprocessing**
   - Historical stock data is downloaded from Yahoo Finance.
   - Technical indicators (RSI, CCI, VWAP, ROC) are calculated.
   - Trade signals are generated based on these indicators.

2. **Data Preparation**
   - Columns used for generating signals (RSI, CCI, VWAP, ROC) are dropped to avoid data leakage.
   - Data is split into training and testing sets.
   - Features are scaled using MinMaxScaler to normalize values for LSTM input.

3. **LSTM Model**
   - An LSTM model is constructed using TensorFlow/Keras.
   - The model architecture includes LSTM layers with Dropout for regularization.
   - Training data is fed into the model to learn patterns in stock price movements.

4. **Evaluation Metrics**
   - **Sharpe Ratio:** Measures the risk-adjusted return of the model's predictions relative to the risk-free rate.
   - **Root Mean Square Error (RMSE):** Quantifies the prediction error between actual and predicted stock prices.
   - **Correlation:** Assesses the linear relationship between predicted and actual stock price movements.

