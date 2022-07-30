import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv("onlyE_LS4.log", " ", names=['Fibril', 'Sandwich', 'Tetramer'])

print(df1)

fig = plt.figure()
#df.boxplot()

sns.boxplot(x="variable", y="value", data=pd.melt(df1))

plt.ylim(-12.2,-5.8)
plt.ylabel('Energy (kcal/mol)', fontsize=16)
plt.title('LS4 binding in fibril and oligomer', fontsize=16)
#plt.show()
plt.savefig('energy_box_LS4.png')
