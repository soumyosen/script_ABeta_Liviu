import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_LSP = pd.read_csv("energy_LSP.traj")
df_LS4_PI = pd.read_csv("energy_LS4_PI.traj")
#df_LS4_FI = pd.read_csv("energy_LS4_FI.traj")

df_LSP.columns = pd.MultiIndex.from_product([df_LSP.columns, ['LSP']])
df_LS4_PI.columns = pd.MultiIndex.from_product([df_LS4_PI.columns, ['LS4_PI']])
#df_LS4_FI.columns = pd.MultiIndex.from_product([df_LS4_FI.columns, ['LS4_FI']])

df_LSP.columns = df_LSP.columns.swaplevel(0, 1)
df_LS4_PI.columns = df_LS4_PI.columns.swaplevel(0, 1)
#df_LS4_FI.columns = df_LS4_FI.columns.swaplevel(0, 1)

#print(df_LSP.head())
#print(df_LS4_PI.head())
#print(df_LS4_FI.head())

#df = pd.concat([df_LSP, df_LS4_PI, df_LS4_FI], axis=1)
df = pd.concat([df_LSP, df_LS4_PI], axis=1)
print(df.head())

#print(df["LSP"]["Elec"])
#print(df["LSP"]["VdW"])

LSP_elec_mean = df["LSP"]["Elec"].mean()
LSP_vdw_mean = df["LSP"]["VdW"].mean()
LS4_PI_elec_mean = df["LS4_PI"]["Elec"].mean()
LS4_PI_vdw_mean = df["LS4_PI"]["VdW"].mean()
#LS4_FI_elec_mean = df["LS4_FI"]["Elec"].mean()
#LS4_FI_vdw_mean = df["LS4_FI"]["VdW"].mean()

LSP_elec_std = df["LSP"]["Elec"].std()
LSP_vdw_std = df["LSP"]["VdW"].std()
LS4_PI_elec_std = df["LS4_PI"]["Elec"].std()
LS4_PI_vdw_std = df["LS4_PI"]["VdW"].std()
#LS4_FI_elec_std = df["LS4_FI"]["Elec"].std()
#LS4_FI_vdw_std = df["LS4_FI"]["VdW"].std()


#systems = ["pre-LS4", "LS4_PI", "LS4_FI"]
systems = ["LS4", "pre-LS4"]
x_pos = np.arange(len(systems))
elec_mean = [LS4_PI_elec_mean, LSP_elec_mean]
vdw_mean = [LS4_PI_vdw_mean, LSP_vdw_mean]
elec_std = [LS4_PI_elec_std, LSP_elec_std]
vdw_std = [LS4_PI_vdw_std, LSP_vdw_std] 

width = 0.35
fig, ax = plt.subplots()
ax.bar(x_pos-width/2, elec_mean, yerr=elec_std, width=width, color='red', ecolor='black', capsize=10, label="Elec")
ax.bar(x_pos+width/2, vdw_mean, yerr=vdw_std, width=width, color='green', ecolor='black', capsize=10, label="VdW")
ax.set_ylabel('Energy (kcal/mol)', fontsize=16)
ax.set_xticks(x_pos)
ax.set_xticklabels(systems, fontsize=16)
leg=ax.legend(loc=4, fontsize=12)
for line in leg.get_lines():
    line.set_linewidth(2)

#plt.show()
plt.savefig("diff_energy_barplot3.png", dpi=400)
