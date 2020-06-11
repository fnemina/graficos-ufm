import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(columns=2, fontawesome=True, siunitx=True)

# Grafico
fig = plt.figure(figsize=(6.9,3))

x = np.linspace(0,1,300)
def y(x, x0, d):
    z = np.exp(-(x-x0)**2/d**2)
    return z
plt.plot(x, y(x,0.2,0.1),"C0")
plt.plot(x, y(x,0.5,0.1),"C0")

plt.text(0.2,0.4,s=r"\large Ancho de banda",bbox=dict(facecolor='white', edgecolor='none', pad=1.5,boxstyle='round,pad=0.5'),horizontalalignment='center',verticalalignment='center',rotation=0)
plt.annotate("",(0.111,0.5),(0.289,0.5), 
            arrowprops=dict(color='k', arrowstyle="<->", lw=2))

plt.text(0.35,1.1,s=r"\large Intervalo de muestreo",horizontalalignment='center',verticalalignment='center',rotation=0)
plt.annotate("",(0.2,1.05),(0.5,1.05), 
            arrowprops=dict(color='k', arrowstyle="<->", lw=2))
# Configuracion ejes

plt.xlabel("Longitud de onda")
plt.ylabel("Respuesta del sensor")
plt.xticks([], [])
plt.yticks([], [])


plt.plot(x, y(x,0.9,0.05),"C3")
plt.plot(x, y(x,0.8,0.05),"C3")

plt.ylim(bottom=0,top=1.2)

plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-spectral.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-spectral.png", dpi=300)
