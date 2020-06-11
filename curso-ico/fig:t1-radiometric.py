import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(columns=2, fontawesome=True, siunitx=True)

# Grafico
fig = plt.figure(figsize=(6.9,3))

x = np.linspace(0,1)
def y(x):
    z = 2*x
    z[x<0.2] = 2*0.2
    z[x>0.8] = 2*0.8
    return z
plt.plot(x, y(x))
plt.plot(x, 2*x, ":", alpha=0.5)

# Configuracion ejes

plt.xlabel("Radiancia")
plt.xticks([0.2, 0.8], [r"$L_{min}$", r"$L_{max}$"])
plt.ylabel("DN")
plt.yticks([0.4, 1.6], [r"$0$", r"$2^N-1$"])


plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-radiometric0.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-radiometric0.png", dpi=300)


plt.annotate("",(0.05,0.4),(0.05,0.1), 
            arrowprops=dict(color='C2', arrowstyle="<-", lw=1))

plt.annotate("",(0.95,1.6),(0.95,0.95*2), 
            arrowprops=dict(color='C2', arrowstyle="<-", lw=1))

plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-radiometric1.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-radiometric1.png", dpi=300)
plt.close()
# Grafico
fig = plt.figure(figsize=(6.9,3))

x = np.linspace(0,1)

plt.plot(x, y(x))
plt.plot(x, 2*x, ":", alpha=0.5)

# Configuracion ejes

plt.xlabel("Radiancia")
plt.xticks([0.2, 0.8], [r"$L_{min}$", r"$L_{max}$"])
plt.ylabel("DN")
plt.yticks([0.4, 1.6], [r"$0$", r"$2^N-1$"])

plt.tight_layout()

plt.text(0.5,0.3,s=r"\large Rango dinámico",horizontalalignment='center',verticalalignment='center',rotation=0)
plt.annotate("",(0.2,0.2),(0.8,0.2), 
            arrowprops=dict(color='k', arrowstyle="|-|", lw=1))

plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-radiometric2.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-radiometric2.png", dpi=300)

plt.text(0.1,1.0,s=r"\large Número de bits",horizontalalignment='left',verticalalignment='center',rotation=0)
plt.annotate("",(0.05,0.4),(0.05,1.6), 
            arrowprops=dict(color='k', arrowstyle="|-|", lw=1))

plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-radiometric3.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-radiometric3.png", dpi=300)
plt.close()