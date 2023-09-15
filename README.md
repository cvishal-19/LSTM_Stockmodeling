# Stock Predictor Web App

## Overview

This Stock Predictor Web App is a powerful tool for analyzing and predicting stock trends using Long Short-Term Memory (LSTM) neural networks. Built with Python, this web app leverages the Streamlit framework for creating an intuitive and user-friendly interface.

## Features

- **Historical Data Analysis**: Access historical stock data spanning over a decade (2010 to 2023) for a wide range of stock symbols.
- **Interactive Interface**: Users can input their desired stock symbol to retrieve and analyze historical price trends.
- **LSTM Model**: The web app uses a pre-trained LSTM model to make predictions on future stock prices.
- **Visualization**: Visualize historical stock data, predicted prices, and trends through interactive charts and graphs.
- **Future Predictions**: Get predictions for the next 100 days to assist in decision-making.

## Getting Started

1. Clone the repository to your local machine.
2. Run the app using `streamlit run app.py`.
3. Input your preferred stock symbol and explore historical data and predictions.

## How It Works

1. Historical Data: The app downloads historical stock data from Yahoo Finance, enabling users to analyze trends.

2. Data Preprocessing: Data is split into training and testing sets, scaled using MinMaxScaler, and prepared for LSTM input.

3. LSTM Model: A pre-trained LSTM model is loaded to predict future stock prices.

4. Visualization: Users can view historical data and predictions through interactive charts.

## Acknowledgments

- This project was developed by Me.
- The LSTM model was trained on the scrapped dataset from Yahoo finance.

## Feedback and Contributions

Contributions and feedback are welcome! If you find issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

