import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(columns=2, fontawesome=True)

# Grafico
fig = plt.figure(figsize=(6.9,3))
ax1 = fig.add_subplot(111)
xmax = 8*np.pi
ymax = xmax/((6.9/3))
ax1.set_xlim(0-1.2,xmax)
ax1.set_ylim(0,ymax)

# EM waves
x = np.linspace(0-0.85, 19*xmax/20,200)+xmax/30
ax1.plot(x, ymax/4*np.sin(x)+ymax/2, "C0")
ax1.plot(x, ymax/4*np.sin(x)*0+ymax/2, ":k", lw=1, alpha=0.25)
ax1.plot(x+np.sin(-x), -ymax/8*np.sin(x)+ymax/2, color="C3", alpha=0.5)

# Patches
ax1.annotate(r"\large$\hat{z}$", xy=(xmax/22-1.2, ymax/2), 
                              xytext=(3*xmax/20-1.2, ymax/2),
            arrowprops=dict(facecolor='black', arrowstyle="<-"),
            va="center", ha="center")

ax1.annotate(r"\large$\hat{x}$", xy=(xmax/20-1.2, ymax/2.02), 
                              xytext=(xmax/20-1.2, ymax/2+1.1*xmax/10),
            arrowprops=dict(facecolor='black', arrowstyle="<-"),
            va="center", ha="center")

ax1.annotate(r"\large$\hat{y}$", xy=(xmax/19-1.2, ymax/1.98), 
                              xytext=(xmax/20-0.9*xmax/10/1.41-1.2, ymax/2-0.9*xmax/10/1.41),
            arrowprops=dict(facecolor='black', arrowstyle="<-"),
            va="center", ha="center")
# Texto
ax1.text(xmax/8,7.25*ymax/9,s=r"\large$E(z-\omega t)$",horizontalalignment='right', verticalalignment='center_baseline')
ax1.text(xmax/8-1,ymax/3,s=r"\large$B(z-\omega t)$",horizontalalignment='right', verticalalignment='center_baseline')
ax1.annotate('', xy=(2*np.pi+np.pi/2, 7.25*ymax/9), 
                xytext=(4*np.pi+np.pi/2, 7.25*ymax/9),
            arrowprops=dict(facecolor='black', arrowstyle="|-|"))
ax1.text(3*np.pi+np.pi/2,7.65*ymax/9,s=r"\large$\lambda$",horizontalalignment='center', verticalalignment='center_baseline')

ax1.axis('off')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t1-wave.pdf")
plt.savefig("curso-ico/figs/fig:t1-wave.png", dpi=300)