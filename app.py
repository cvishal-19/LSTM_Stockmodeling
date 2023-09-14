import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as yf
import datetime as dt
import streamlit as st
from keras.models import load_model


start = dt.datetime(2010, 1, 1)
end = dt.datetime(2023, 1, 1)

st.title("stock trend model")

user_input = st.text_input("Enter stock", 'AAPL')
df = yf.download(user_input, start=start, end=end)


st.subheader("Data from 2010 to 2023")
st.write(df.describe())

st.subheader("Closing price vs Time")
fig = plt.figure(figsize = (20,12))
plt.plot(df.Close)
st.pyplot(fig)

data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.60)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.60):int(len(df))])
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
data_training_array = scaler.fit_transform(data_training)





model = load_model('keras_model.h5')

past_100_days = data_training.tail(100)
final_df = past_100_days.append(data_testing, ignore_index= True)
input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100 : i])
    y_test.append(input_data[i, 0 ])

x_test, y_test = np.array(x_test) , np.array(y_test)
y_predicted = model.predict(x_test)



a = scaler.scale_
scaler_factor = 1/a
y_predicted = y_predicted * scaler_factor
y_test = y_test * scaler_factor


st.subheader("prediction vs original")
fig2 = plt.figure(figsize = (20,12))
plt.plot(y_test, 'b', label = 'original price')
plt.plot(y_predicted, 'r', label = 'predicted price')
plt.xlabel('Time')
plt.ylabel('price')
plt.legend()
st.pyplot(fig2)

