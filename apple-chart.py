import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
APPL = pd.read_csv('APPL.csv')
APPL

plt.style.use('fivethirtyeight')

plt.figure(figsize=(12.5, 4.5))
plt.plot(APPL['Adj Close'], label = 'APPL')
plt.title('APPL Adj. Close Price History')
plt.xlabel('Mar. 06, 2020 - Mar 05, 2021')
plt.ylabel('Adj. Close Price USD($)')
plt.legend(loc='upper left')
plt.show()

# create 30 day SMA
# create 30 day SMA
SMA30 = pd.DataFrame()
SMA30['Adj Close'] = APPL['Adj Close'].rolling(window= 9).mean()
SMA30

#dreate 100 day SMA
SMA100 = pd.DataFrame()
SMA100['Adj Close'] = APPL['Adj Close'].rolling(window=27).mean()
SMA100

#visualisation
plt.figure(figsize=(12.5, 4.5))
plt.plot(APPL['Adj Close'], label = 'APPL')
plt.plot(SMA30['Adj Close'], label = 'SMA30')
plt.plot(SMA100['Adj Close'], label = 'SMA100')
plt.title('APPL Adj. Close Price History')
plt.xlabel('Mar. 06, 2020 - Mar 05, 2021')
plt.ylabel('Adj. Close Price USD($)')
plt.legend(loc='upper left')
plt.show()

#create a new data fram to store data
data = pd.DataFrame()
data['APPL'] = APPL['Adj Close']
data['SMA30'] = SMA30['Adj Close']
data['SMA100'] = SMA100['Adj Close']
data

#create a function that will return buy and sell price to plot on chart
def buy_sell(data):
  sigPriceBuy = []
  sigPriceSell =[]
  flag = -1

  for i in range(len(data)):
    if data ['SMA30'][i] > data['SMA100'][i]:
      if flag != 1:
        sigPriceBuy.append(data['APPL'][i])
        sigPriceSell.append(np.nan)
        flag = 1
      else: 
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    elif data['SMA30'][i] < data['SMA100'][i]:
      if flag != 0:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(data['APPL'][i])
        flag = 0
      else: 
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    else:
      sigPriceBuy.append(np.nan)
      sigPriceSell.append(np.nan)

  return (sigPriceBuy, sigPriceSell)

  # store buy and sell flags in a var
  buy_sell = buy_sell(data) 
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

#visualized the data and teh strategety to buy and sell
plt.figure(figsize=(12.5, 4.5))
plt.plot(data['APPL'], label = ['APPL'], alpha = 0.35)
plt.plot(data['SMA30'], label ='SMA30', alpha = 0.35)
plt.plot(data['SMA100'], label = 'SMA100', alpha = 0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker = 'v', color = 'red')
plt.title('Apple Adj. Close Hisory Buy & Sell Signals')
plt.xlabel('Mar 06, 2020 - Mar 05, 2021')
plt.ylabel('Adj close Price USD ($)')
plt.legend(loc='upper left')
plt.show()
