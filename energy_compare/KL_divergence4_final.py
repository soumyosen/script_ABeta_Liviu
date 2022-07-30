import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, zscore, ks_2samp, entropy
from scipy.spatial import distance


df1 = pd.read_csv("only_energy_LS4.log", " ", names=['Energy'])
df2 = pd.read_csv("only_energy_LSP.log", " ", names=['Energy'])

#df = pd.concat([df1, df2], axis=1, sort=False)

weights1 = np.ones_like(df1["Energy"])/float(len(df1["Energy"]))
weights2 = np.ones_like(df2["Energy"])/float(len(df2["Energy"]))
bins = np.linspace(-13.0, -6.0, 700)

ndf1, bin_1 = np.histogram(df1["Energy"], bins=bins, range=None, normed=None, weights=weights1, density=None)
ndf2, bin_2 = np.histogram(df2["Energy"], bins=bins, range=None, normed=None, weights=weights2, density=None)

ndf1 = ndf1 + 0.0000000000001
ndf2 = ndf2 + 0.0000000000001

####### Here we are calculating JS distance which is square roor of JS divergence. The value is close to 1 when two distributions
####### are different and the value is close to 0 when two distributions are same. The entropy is calculated by base 2.0.

print("JS distance for docking energy distribution")
print(distance.jensenshannon(ndf1, ndf2, 2.0))

