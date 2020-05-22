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
x = [xmax/2-0.02,xmax/2+0.02,xmax/2+0.01,xmax/2-0.01]
y = [ymax/3-0.01,ymax/3-0.01,ymax/3+0.01,ymax/3+0.01]
ax1.add_patch(patches.Polygon(xy=list(zip(x,y)), facecolor="C3", alpha=0.5))


ax1.axes.add_patch(
    patches.Arc((xmax/2, ymax/3), width=0.4, 
    height=0.4, theta1=0, theta2=180,linewidth=2
    )
)

ax1.axes.add_patch(
    patches.Arc((xmax/2, ymax/3), width=0.4, 
    height=0.15, theta1=180, theta2=360,linewidth=1
    )
)
ax1.axes.add_patch(
    patches.Arc((xmax/2, ymax/3), width=0.4, 
    height=0.15, theta1=0, theta2=180,linewidth=1, linestyle=":"
    )
)

# Lineas
r = 0.15
a = np.pi/4
plt.plot([xmax/2,xmax/2+r*np.cos(a)],[ymax/3,ymax/3+r*np.sin(a)],"C0",lw=2)
r = 0.15
a = 1.3*np.pi/4
plt.plot([xmax/2,xmax/2+r*np.cos(a)],[ymax/3,ymax/3+r*np.sin(a)],"C0",lw=2)

r = 0.15
a = 1.15*np.pi/4
ax1.axes.add_patch(
    patches.Ellipse((xmax/2+r*np.cos(a), ymax/3+r*np.sin(a)), width=0.018, 
    height=0.038, angle=50,linewidth=0, color="C0", alpha=0.5
    )
)

r = 0.8
a = 1.15*np.pi/4
plt.plot([xmax/2,xmax/2+r*np.cos(a)],[ymax/3,ymax/3+r*np.sin(a)],":k",lw=1)

ax1.axes.add_patch(
    patches.Arc((xmax/2, ymax/3), width=0.45, 
    height=0.45, theta1=a*180/np.pi, theta2=90,linewidth=2, linestyle="-", color="C2"
    )
)

r = 0.8
a = np.pi/2
plt.plot([xmax/2,xmax/2+r*np.cos(a)],[ymax/3,ymax/3+r*np.sin(a)],"k",lw=1)

r = 0.8
a = np.pi/4
plt.plot([xmax/2,xmax/2+r*np.cos(a)],[ymax/3,ymax/3+r*np.sin(a)],":C0",lw=1)
r = 0.8
a = 1.3*np.pi/4
plt.plot([xmax/2,xmax/2+r*np.cos(a)],[ymax/3,ymax/3+r*np.sin(a)],":C0",lw=1)

# Texto
r = 0.15
a = 0.8*np.pi/4
ax1.text(.95*xmax/2,ymax/3,s=r"\large$A$",horizontalalignment='right', verticalalignment='center_baseline')
ax1.text(xmax/2+r*np.cos(a),ymax/3+r*np.sin(a),s=r"\large$\Omega$",horizontalalignment='center', verticalalignment='center_baseline')
r = 0.25
a = ((2-1.15)/2+1.15)*np.pi/4
ax1.text(xmax/2+r*np.cos(a),ymax/3+r*np.sin(a),s=r"\large$\theta$",horizontalalignment='center', verticalalignment='center_baseline')

ax1.axis('off')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t1-angles.pdf")
plt.savefig("curso-ico/figs/fig:t1-angles.png", dpi=300)