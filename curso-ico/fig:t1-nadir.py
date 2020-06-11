import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(columns=2, fontawesome=True, siunitx=True)

# Grafico
fig = plt.figure(figsize=(6.9,3))
ax1 = fig.add_subplot(111)

t = np.linspace(-8,8,200)
plt.fill_between(0.5*t+np.cos(0.5*(t+np.pi/4)),np.cos(8*t)/128-0.01, 0*t-2, color="C0",linewidth=0.0,alpha=0.25)

ax1.text(0.51,0.85,s=r"\Huge\faIcon{satellite}",horizontalalignment='center',verticalalignment='center',rotation=135)

# NADIR

plt.plot((0.51,0.51),(0.85,0),'k-',alpha=0.3)

ax1.text(0.475,0.3,s=r'\normalsize Nadir',horizontalalignment='center',verticalalignment='center')

# Configuracion ejes
plt.ylim(-.1,1)
plt.yticks([])
plt.xticks([])

plt.xlim(0,1)
ax1.axis('off')
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-spatial-0.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-spatial-0.png", dpi=300)
plt.close()