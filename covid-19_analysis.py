import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {'family':'AppleGothic'}
matplotlib.rc('font', **font)

# pands
data = pd.read_csv("/Users/kataokakenta/Desktop/COVID-19.csv")
data_shizuoka = data.query("受診都道府県 == '東京都'").groupby("確定日").count().iloc[:,[0]]
# print(data_shizuoka.index)
# print(data_shizuoka.iloc[:,[0]])
data_shizuoka.plot()
# print(data_shizuoka.groupby("確定日").count().iloc[:,[0]])

# matplot
plt.title("Dairy add confirmed")
plt.xlabel("Date")
plt.ylabel("Add confirmed")
plt.grid(True)
plt.legend()

# plt.bar(nd_data_x, nd_data_y)
plt.show()