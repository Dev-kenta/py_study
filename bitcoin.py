import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

btc_price = pd.read_csv('/Users/kataokakenta/Desktop/coindesk-bpi-USD-close_data-2018-06-07_2018-06-27.csv')
# print(btc_price.head())

X = btc_price.loc[0:499, ["Close Price"]]
y = btc_price.loc[1:500, ["Close Price"]]
X_train = np.array(X[:400])
X_test  = np.array(X[400:])
y_train = np.array(y[:400])
y_test  = np.array(y[400:])

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 学習結果
# print(y_pred)
# テストデータ
# print(y_test)
# グラフを生成して予測
plt.plot(range(0,100), y_test, label='Actual price', color='blue')
plt.plot(range(0,100), y_pred, label='Predicted price', color='red')
plt.xlabel('Hours')
plt.ylabel('Price ($)')
plt.title('Bitcoin Price')
plt.grid(True)
plt.legend(loc = "upper left")
plt.show()