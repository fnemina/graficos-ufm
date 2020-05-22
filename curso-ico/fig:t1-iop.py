import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(columns=2, fontawesome=True)

# Grafico
fig = plt.figure(figsize=(6.9,3))
ax1 = fig.add_subplot(111)
xmax = 1
ymax = xmax/((6.9/3))
ax1.set_xlim(0,xmax)
ax1.set_ylim(0,ymax)

# Patches
ax1.axes.add_patch(
    patches.Circle(
        (xmax/2, ymax/3),   # (x,y)
        xmax/10,          # width
        facecolor="C0",
        linewidth=0,
        alpha=0.5
    )
)

ax1.axes.add_patch(
    patches.Arrow(
        xmax/8, ymax/3,   # (x,y)
        0.25,0,width=0.1,      # width
        facecolor="C0",
        linewidth=0,
    )
)

ax1.axes.add_patch(
    patches.Arrow(
        xmax/2+xmax/8, ymax/3,   # (x,y)
        0.25,0,width=0.07,      # width
        facecolor="C0", alpha=0.5,
        linewidth=0,
    )
)

ax1.axes.add_patch(
    patches.Arrow(
        xmax/2+np.cos(np.pi/4)*xmax/8, ymax/3+np.sin(np.pi/4)*xmax/8,   # (x,y)
        0.25/np.sqrt(2),0.25/np.sqrt(2),width=0.05,      # width
        facecolor="C0", alpha=0.5,
        linewidth=0,
    )
)

ax1.axes.add_patch(
    patches.Arc((xmax/2, ymax/3), width=0.5, 
    height=0.5, theta1=5, theta2=40,linewidth=2
    )
)

ax1.annotate('', xy=(xmax/2-xmax/10, 0), 
                              xytext=(xmax/2+xmax/10, 0),
            arrowprops=dict(facecolor='black', arrowstyle="|-|"))
ax1.text(xmax/2,ymax/20,s=r"\large$\Delta r$",horizontalalignment='center', verticalalignment='center_baseline')
# Texto
ax1.text(xmax/8,ymax/3,s=r"\large$\Phi_i(\lambda)$",horizontalalignment='right', verticalalignment='center_baseline')
ax1.text(xmax/2,ymax/3,s=r"\large$\Phi_a(\lambda)$",horizontalalignment='center', verticalalignment='center_baseline')
ax1.text(xmax/2+xmax/8+0.25,ymax/3,s=r"\large$\Phi_t(\lambda)$",horizontalalignment='left', verticalalignment='center_baseline')
ax1.text(xmax/2+np.cos(np.pi/4)*xmax/8+0.25/np.sqrt(2),
         ymax/3+np.sin(np.pi/4)*xmax/8+0.25/np.sqrt(2),s=r"\large$\Phi_s(\lambda, \chi)$",horizontalalignment='left', verticalalignment='center_baseline')

ax1.text(xmax/2+np.cos(np.pi/8)*xmax/3.5,
         ymax/3+np.sin(np.pi/8)*xmax/3.5,s=r"\large$\chi$",horizontalalignment='left', verticalalignment='center_baseline')
ax1.axis('off')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t1-iop.pdf")
plt.savefig("curso-ico/figs/fig:t1-iop.png", dpi=300)