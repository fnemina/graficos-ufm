import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(fig_width=5, fontawesome=True, siunitx=True)

# FROM OSOAA manual
# 4.3.3.2 Sea molecule profile
g = 0.069
chl_range = [0.001,0.01,0.1,1,10]
# Grafico
x = np.linspace(400, 700)
for chl in chl_range:
    bb = 0.03*(550/x)*chl**(0.62)
    plt.plot(x, bb, label=f"{chl}"+r"\si{\milli\gram\per\cubic\meter}")

plt.ylabel(r"$b_b$ [\si{\per\meter}]")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-chl-bb.pdf")
plt.savefig("curso-ico/figs/fig:t2-chl-bb.png", dpi=300)
plt.close()

# Grafico
data = np.loadtxt("data/OSOAA_SEA_PHYT_COEFFS.txt")
AP = np.interp(x, data[:,0], data[:,1])
EP = np.interp(x, data[:,0], data[:,2])
for chl in chl_range:
    a = AP*chl**EP
    plt.plot(x, a, label=f"{chl}"+r"\si{\milli\gram\per\cubic\meter}")
#plt.yscale("log")
#plt.yticks([0.001,0.01,0.1,1,10,100], [0.001,0.01,0.1,1,10,100])
plt.ylabel(r"$a$ [\si{\per\meter}]")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-chl-a.pdf")
plt.savefig("curso-ico/figs/fig:t2-chl-a.png", dpi=300)
plt.close()

# Grafico
for chl in chl_range:
    bb = 0.03*(550/x)*chl**(0.62)
    a = AP*chl**EP
    plt.plot(x, g*bb/(a+bb), label=f"{chl}"+r"\si{\milli\gram\per\cubic\meter}")
plt.ylabel(r"$R$ ")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-chl-R.pdf")
plt.savefig("curso-ico/figs/fig:t2-chl-R.png", dpi=300)
plt.close()


