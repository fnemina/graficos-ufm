import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(fig_width=5, fontawesome=True, siunitx=True)

# Selected Papers from the 14th Estuarine and Coastal Modeling Conference
g = 0.069

nap_range = np.logspace(-3,2,6)
S_range = [0.06,0.08,0.10,0.12]
g_range = np.round(np.linspace(-3,-.8,5),1)
x0 = 440
nap = 40
# Grafico
x = np.linspace(400, 700)
bbw = 0.00288*(x/500)**(-4.32)
for gbb in g_range:
    bb = 0.604*nap**(0.766)
    bb = bb*(x/550)**(gbb)
    plt.plot(x, bb+bbw, label=f"{gbb}")

plt.ylabel(r"$b_b$ [\si{\per\meter}]")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-waternap-bb.pdf")
plt.savefig("curso-ico/figs/fig:t2-waternap-bb.png", dpi=300)
plt.close()

# Grafico
dataw = np.loadtxt("data/OSOAA_SEA_MOL_COEFFS_JUNE_2013.txt")
aw = np.interp(x, dataw[:,0], dataw[:,1])
for S in S_range:
    a = 0.095*nap**(0.626)
    a = a*np.exp(-S*(x-x0))
    plt.plot(x, a+aw, label=f"{S}"+r"\si{\per\nano\meter}")
#plt.yscale("log")
#plt.yticks([0.001,0.01,0.1,1,10,100], [0.001,0.01,0.1,1,10,100])
plt.ylabel(r"$a$ [\si{\per\meter}]")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-waternap-a.pdf")
plt.savefig("curso-ico/figs/fig:t2-waternap-a.png", dpi=300)
plt.close()

# Grafico
plt.plot(x, g*(bbw)/(aw+bbw), "k-.", label=f"Agua")
for nap in nap_range:
    bb = 0.604*nap**(0.766)
    bb = bb*(x/550)**(-0.8)
    a = 0.095*nap**(0.626)
    a = a*np.exp(-0.06*(x-x0))
    plt.plot(x, g*(bb+bbw)/(a+bb+aw+bbw), label=f"{nap}"+r"\si{\milli\gram\per\liter}")

plt.ylabel(r"$R$ ")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-waternap-R.pdf")
plt.savefig("curso-ico/figs/fig:t2-waternap-R.png", dpi=300)
plt.close()