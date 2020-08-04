import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(fig_width=5, fontawesome=True, siunitx=True)

# FROM OSOAA manual
# Modeling Water Clarity and Light Quality in Oceans
g = 0.069
# Grafico
x = np.linspace(400, 700)
x0 = 440
# Grafico
S_range = np.linspace(0.01,0.02,5)
for S in S_range:
    a = 0.01
    a = a*np.exp(-S*(x-x0))
    plt.plot(x, a, label=f"{S:0.4f}"+r"\si{\per\nano\meter}")
#plt.yscale("log")
#plt.yticks([0.001,0.01,0.1,1,10,100], [0.001,0.01,0.1,1,10,100])
plt.ylabel(r"$a$ [\si{\per\meter}]")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-cdom-a.pdf")
plt.savefig("curso-ico/figs/fig:t2-cdom-a.png", dpi=300)
plt.close()


# Grafico
dataw = np.loadtxt("data/OSOAA_SEA_MOL_COEFFS_JUNE_2013.txt")
aw = np.interp(x, dataw[:,0], dataw[:,1])
bbw = 0.00288*(x/500)**(-4.32)
# Grafico
S_range = np.linspace(0.01,0.02,5)
plt.plot(x, g*(bbw)/(aw+bbw), "k-.", label=f"Agua")
for S in S_range:
    a = 0.01
    a = a*np.exp(-S*(x-x0))
    plt.plot(x, g*(bbw)/(aw+a+bbw), label=f"{S:0.4f}"+r"\si{\per\nano\meter}")
plt.ylabel(r"$R$ ")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-watercdom-R.pdf")
plt.savefig("curso-ico/figs/fig:t2-watercdom-R.png", dpi=300)
plt.close()