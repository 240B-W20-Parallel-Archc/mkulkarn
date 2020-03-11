import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("./latencyLog2.csv")
df["log2array"] = np.log2(df["size"])

dfx = df[df['cores'] == 1]
dfx = dfx[dfx['Sequential'] == 0]
dfx = dfx[dfx['modify'] == 0]

ax = dfx.plot(x='log2array', y='latency', c='r')

c = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'brown', 'darkslategray', 'navy', 'plum']
for i in range(2,12):
	dfx = df[df['cores'] == i]
	dfx = dfx[dfx['Sequential'] == 0]
	dfx = dfx[dfx['modify'] == 0]

	dfx.plot(x='log2array', y='latency', c=c[i-1], ax=ax)

dfx = df[df['cores'] == 1]
dfx = dfx[dfx['Sequential'] == 1]
dfx = dfx[dfx['modify'] == 0]

ax1 = dfx.plot(x='log2array', y='latency', c='r')
for i in range(2,12):
	dfx = df[df['cores'] == i]
	dfx = dfx[dfx['Sequential'] == 1]
	dfx = dfx[dfx['modify'] == 0]

	dfx.plot(x='log2array', y='latency', c=c[i-1], ax=ax1)

dfx = df[df['cores'] == 1]
dfx = dfx[dfx['Sequential'] == 0]
dfx = dfx[dfx['modify'] == 1]

ax2 = dfx.plot(x='log2array', y='latency', c='r')
for i in range(2,12):
	dfx = df[df['cores'] == i]
	dfx = dfx[dfx['Sequential'] == 0]
	dfx = dfx[dfx['modify'] == 1]

	dfx.plot(x='log2array', y='latency', c=c[i-1], ax=ax2)
plt.show()