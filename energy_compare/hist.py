import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("only_energy_LS4.log", " ", names=['Energy'])
df2 = pd.read_csv("only_energy_LSP.log", " ", names=['Energy'])

df1_med = df1["Energy"].median()
df2_med = df2["Energy"].median()

weights1 = np.ones_like(df1["Energy"])/float(len(df1["Energy"]))
weights2 = np.ones_like(df2["Energy"])/float(len(df2["Energy"]))
bins = np.linspace(-13.0, -6.0, 700)

fig = plt.figure()

plt.hist(df1["Energy"], bins, weights=weights1, alpha=0.3, color='red', label="LS4")
plt.hist(df2["Energy"], bins, weights=weights2, alpha=0.3, color='blue', label="LSP")
plt.xlabel('Energy (kcal/mol)', fontsize=16)
plt.ylabel('Normalized Counts', fontsize=16)
plt.xlim(-13.0,-6.0)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.axvline(x=df1_med, color='red', linestyle=':')
plt.axvline(x=df2_med, color='blue', linestyle=':')

plt.show()

