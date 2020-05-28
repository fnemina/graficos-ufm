import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(columns=2, fontawesome=True, siunitx=True)

# Grafico
fig = plt.figure(figsize=(6.9,3))
ax1 = fig.add_subplot(111)
xmax = 2
ymax = xmax/((6.9/3))
ax1.set_xlim(0,xmax)
ax1.set_ylim(0,ymax)

ellipse = patches.Arc(xy=(1, 0.4),width=1.8, height=0.3, 
                        edgecolor='k', fc='w', lw=2,  theta1=0, theta2=360, ls=':',alpha=0.5, angle=5)
ax1.add_patch(ellipse)
ax1.text(1,0.4,s=r"\Huge\faIcon{globe-americas}",
         horizontalalignment='center',
         verticalalignment='center')
ax1.text(0.1,0.32,s=r"\huge\faIcon{satellite}",
         rotation=+45+90+5,
         horizontalalignment='center',
         verticalalignment='center')


ax1.annotate('', xy=(xmax/2+0.05, 0.1), 
                              xytext=(xmax/2+0.9, 0.1),
            arrowprops=dict(facecolor='black', arrowstyle="|-|"))
ax1.text(xmax/2+0.45,ymax/20+0.1,s=r"\large$h\approx\SI{35786}{\kilo\meter}$",horizontalalignment='center', verticalalignment='center_baseline')

ax1.axis('off')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-orbit-geo.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-orbit-geo.png", dpi=300)
plt.close()

# Grafico
fig = plt.figure(figsize=(6.9,3))
ax1 = fig.add_subplot(111)
xmax = 2
ymax = xmax/((6.9/3))
ax1.set_xlim(0,xmax)
ax1.set_ylim(0,ymax)

ellipse = patches.Arc(xy=(1, 0.4),width=0.11, height=0.8, 
                        edgecolor='k', fc='w', lw=2,  theta1=0, theta2=360, ls=':',alpha=0.5, angle=-10)
ax1.add_patch(ellipse)
ax1.text(1,0.4,s=r"\Huge\faIcon{globe-americas}",
         horizontalalignment='center',
         verticalalignment='center')
ax1.text(1.07,0.8,s=r"\huge\faIcon{satellite}",
         rotation=+45-10,
         horizontalalignment='center',
         verticalalignment='center')

ax1.annotate('', xy=(xmax/2+0.2, ymax/2+0.01), 
                              xytext=(xmax/2+0.2, ymax/2+0.38),
            arrowprops=dict(facecolor='black', arrowstyle="|-|"))
ax1.text(xmax/2+0.25,ymax/2+0.2,s=r"\large$h\approx$\SI{282}{\kilo\meter} a \SI{5172}{\kilo\meter}",horizontalalignment='left', verticalalignment='center')



ax1.axis('off')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-orbit-helio.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-orbit-helio.png", dpi=300)
plt.close()