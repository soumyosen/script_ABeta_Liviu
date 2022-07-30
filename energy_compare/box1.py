import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv("onlyE_LS4_clusteredfrm.log", " ", names=['Energy_LS4'])
df2 = pd.read_csv("onlyE_LSP_clusteredfrm.log", " ", names=['Energy_LSP'])

df = pd.concat([df1, df2], axis=1, sort=False)
print(df)

fig = plt.figure()
#df.boxplot()

sns.boxplot(x="variable", y="value", data=pd.melt(df))

plt.ylabel('Energy (kcal/mol)', fontsize=16)
plt.ylim(-13.0,-7.0)
plt.title('LS4 and LSP binding in fibril', fontsize=16)
#plt.show()
plt.savefig('energy_box_clusteredfrm.png')
