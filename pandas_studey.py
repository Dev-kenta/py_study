import pandas as pd
import numpy as np

bank_data = pd.read_csv("/Users/kataokakenta/Desktop/bank.csv",index_col='通し', parse_dates=['通し'])

nd_bank_data = bank_data.values
nd_bank_data_columns = bank_data.columns.values

print(type(bank_data))

print(type(nd_bank_data))
print(nd_bank_data)
print(nd_bank_data_columns)