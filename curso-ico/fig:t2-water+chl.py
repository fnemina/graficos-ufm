import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches
import pandas as pd

# Configuro latexify a dos columnas
latexify(fig_width=5, fontawesome=True, siunitx=True)

# FROM OSOAA manual
# 4.3.3.2 Sea molecule profile
g = 0.069
chl_range = [0.001,0.01,0.1,1,10]
x = np.linspace(400, 700)
# Grafico
bbw = 0.00288*(x/500)**(-4.32)
for chl in chl_range:
    bbc = 0.03*(550/x)*chl**(0.62)
    plt.plot(x, bbw+bbc, label=f"{chl}"+r"\si{\milli\gram\per\cubic\meter}")

plt.ylabel(r"$b_b$ [\si{\per\meter}]")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-waterchl-bb.pdf")
plt.savefig("curso-ico/figs/fig:t2-waterchl-bb.png", dpi=300)
plt.close()

# Grafico
dataw = np.loadtxt("data/OSOAA_SEA_MOL_COEFFS_JUNE_2013.txt")
datac = np.loadtxt("data/OSOAA_SEA_PHYT_COEFFS.txt")
AP = np.interp(x, datac[:,0], datac[:,1])
EP = np.interp(x, datac[:,0], datac[:,2])
aw = np.interp(x, dataw[:,0], dataw[:,1])
for chl in chl_range:
    ac = AP*chl**EP
    plt.plot(x, aw+ac, label=f"{chl}"+r"\si{\milli\gram\per\cubic\meter}")
plt.ylabel(r"$a$ [\si{\per\meter}]")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-waterchl-a.pdf")
plt.savefig("curso-ico/figs/fig:t2-waterchl-a.png", dpi=300)
plt.close()

# Grafico
plt.plot(x, g*(bbw)/(aw+bbw), "k-.", label=f"Agua")
for chl in chl_range:
    bbc = 0.03*(550/x)*chl**(0.62)
    ac = AP*chl**EP
    plt.plot(x, g*(bbw+bbc)/(aw+ac+bbw+bbc), label=f"{chl}"+r"\si{\milli\gram\per\cubic\meter}")
plt.ylabel(r"$R$ ")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-waterchl-R.pdf")
plt.savefig("curso-ico/figs/fig:t2-waterchl-R.png", dpi=300)
plt.close()

# Grafico
df = pd.read_excel("data/fluo_sims_PR05.xlsx")
wl = df.iloc[:,0]
chl01 = df.iloc[:,1]
chl05 = df.iloc[:,2]
chl1 = df.iloc[:,3]
chl5 = df.iloc[:,4]
chl10 = df.iloc[:,5]

bbw = 0.00288*(wl/500)**(-4.32)
aw = np.interp(wl, dataw[:,0], dataw[:,1])
plt.plot(wl, g*(bbw)/(aw+bbw), "k-.", label=f"Agua")
plt.plot(wl, chl01, label=f"{0.1}"+r"\si{\milli\gram\per\cubic\meter}")
plt.plot(wl, chl05, label=f"{0.5}"+r"\si{\milli\gram\per\cubic\meter}")
plt.plot(wl, chl1, label=f"{1}"+r"\si{\milli\gram\per\cubic\meter}")
plt.plot(wl, chl5, label=f"{5}"+r"\si{\milli\gram\per\cubic\meter}")
plt.plot(wl, chl10, label=f"{10}"+r"\si{\milli\gram\per\cubic\meter}")

plt.ylabel(r"$R$ ")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-fluo-R.pdf")
plt.savefig("curso-ico/figs/fig:t2-fluo-R.png", dpi=300)
plt.close()