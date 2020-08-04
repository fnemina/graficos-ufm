import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(fig_width=5, fontawesome=True, siunitx=True)

# FROM OSOAA manual
# 4.3.3.2 Sea molecule profile
g = 0.069
# Grafico
x = np.linspace(400, 700)
bb = 0.00288*(x/500)**(-4.32)
plt.plot(x, bb)

plt.ylabel(r"$b_b$ [\si{\per\meter}]")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-water-bb.pdf")
plt.savefig("curso-ico/figs/fig:t2-water-bb.png", dpi=300)
plt.close()

# Grafico
a_data = np.loadtxt("data/OSOAA_SEA_MOL_COEFFS_JUNE_2013.txt")
a = np.interp(x, a_data[:,0], a_data[:,1])
plt.plot(x, a)
plt.yscale("log")
plt.yticks([0.001,0.01,0.1,1,10,100], [0.001,0.01,0.1,1,10,100])
plt.ylabel(r"$a$ [\si{\per\meter}]")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-water-a.pdf")
plt.savefig("curso-ico/figs/fig:t2-water-a.png", dpi=300)
plt.close()

# Grafico
plt.plot(x, g*bb/(a+bb))
plt.ylabel(r"$R$ ")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-water-R.pdf")
plt.savefig("curso-ico/figs/fig:t2-water-R.png", dpi=300)
plt.close()