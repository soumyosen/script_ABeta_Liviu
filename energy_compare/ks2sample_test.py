import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, zscore, ks_2samp, entropy
from scipy.spatial import distance


df1 = pd.read_csv("only_energy_LS4.log", " ", names=['Energy'])
df2 = pd.read_csv("only_energy_LSP.log", " ", names=['Energy'])

#df = pd.concat([df1, df2], axis=1, sort=False)

d, p = ks_2samp(df1["Energy"],df2["Energy"])

print("KS test D and P value for docking energy")
print(d)
print(p)
