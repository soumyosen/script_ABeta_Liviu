import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("LSP_protcontact_prob.dat", sep=" ", header=None, names=["Residue", "Prob"])

plt.scatter(df["Residue"], df["Prob"], c='Red')
plt.ylim(-0.1, 1.1)
plt.xlim(7, 41)
plt.ylabel("Contact Probability", fontsize=16)
plt.xlabel("Residue", fontsize=16)
plt.xticks(np.arange(8, 41, 4))
plt.grid()
#plt.show()
plt.savefig('LSP_protcontact_prob.png')

