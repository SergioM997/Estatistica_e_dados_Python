import pandas as pd
dataset = pd.read_csv("Credit.csv")

dt = dataset.iloc[:,[1,4,7]].values

from sklearn.preprocessing import StandardScaler, MinMaxScaler

sc = StandardScaler()

x = sc.fit_transform(dt)

SC = MinMaxScaler()

y = sc.fit_transform(dt)

