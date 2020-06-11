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


# SWADTH
x = np.linspace(0.5,0.78)
y = 3*(0.5-x)+0.85
z = 3*(0.5-x)+0.85

plt.plot(1-x,y,'k--',alpha=0.3)
plt.plot(x,z,'k--',alpha=0.3)

plt.annotate("",(0.215,0),(0.785,0),
            arrowprops=dict(color='C2', arrowstyle="|-|", lw=2))

# Configuracion ejes
plt.ylim(-.1,1)
plt.yticks([])
plt.xticks([])

ax1.text(0.50,-0.075,s=r'\normalsize Ancho de barrido',horizontalalignment='center',verticalalignment='center')
ax1.text(0.50,0.3,s=r'\normalsize FOV',horizontalalignment='center',verticalalignment='center')
ax1.axes.add_patch(patches.Wedge((0.5, 0.85), 0.5, -108, -72, width=0.010,color='lightgrey'), )


plt.xlim(0,1)
ax1.axis('off')
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-spatial-1.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-spatial-1.png", dpi=300)


x = np.linspace(0.5,0.652)
y = 5.5*(0.5-x)+0.85
z = 8.5*(0.5-x)+0.85

plt.plot(x,y,'k--',alpha=0.7)
x = np.linspace(0.5,0.6)
z = 8.5*(0.5-x)+0.85
plt.plot(x,z,'k--',alpha=0.7)

plt.annotate("",(0.595,0.-0.0),(0.659,0.-0.0),
            arrowprops=dict(color='C3', arrowstyle="|-|", lw=2))

ax1.axes.add_patch(patches.Wedge((0.5, 0.85), 0.3, -83, -79, width=0.010,color='lightgrey'), )

#ax1.text((0.595+0.659)/2-0.001,-0.075,s=r'\normalsize Pixel',horizontalalignment='center',verticalalignment='center')
ax1.text(0.50,0.55,s=r'\normalsize iFOV',horizontalalignment='center',verticalalignment='center')

# Configuracion ejes
plt.ylim(-.1,1)
plt.yticks([])
plt.xticks([])

plt.xlim(0,1)
ax1.axis('off')
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-spatial-2.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-spatial-2.png", dpi=300)
plt.close()


# Grafico
fig = plt.figure(figsize=(6.9,3))
ax1 = fig.add_subplot(111)

t = np.linspace(-8,8,200)
plt.fill_between(0.5*t+np.cos(0.5*(t+np.pi/4)),np.cos(8*t)/128-0.01, 0*t-2, color="C0",linewidth=0.0,alpha=0.25)

ax1.text(0.51,0.85,s=r"\Huge\faIcon{satellite}",horizontalalignment='center',verticalalignment='center',rotation=135)

# SWADTH
x = np.linspace(0.5,0.78)
y = 3*(0.5-x)+0.85
z = 3*(0.5-x)+0.85

plt.plot(1-x,y,'k--',alpha=0.3)
plt.plot(x,z,'k--',alpha=0.3)

# Configuracion ejes
plt.ylim(-.1,1)
plt.yticks([])
plt.xticks([])

ax1.axes.add_patch(patches.Wedge((0.5, 0.85), 0.3, -92, -88, width=0.010,color='C2', alpha=0.5), )
x = np.linspace(0.5-0.028,0.5)
y = -30.5*(0.5-x)+0.85
plt.plot(x,y,'k--',alpha=0.7)
x = np.linspace(0.5,0.5+0.028)
z = 30.5*(0.5-x)+0.85
plt.plot(x,z,'k--',alpha=0.7)

plt.annotate("",(0.531,0.-0.01),(0.5-0.031,0.-0.01),
            arrowprops=dict(color='C2', arrowstyle="|-|", lw=2))

ax1.axes.add_patch(patches.Wedge((0.5, 0.85), 0.3, -76, -72, width=0.010,color='C3', alpha=0.5), )
x = np.linspace(0.5,0.72)
y = 4*(0.5-x)+0.85
plt.plot(x,y,'k--',alpha=0.7)
x = np.linspace(0.5,0.79)
z = 3*(0.5-x)+0.85
plt.plot(x,z,'k--',alpha=0.7)

plt.annotate("",(0.792,0.-0.01),(0.71,0.-0.01),
            arrowprops=dict(color='C3', arrowstyle="|-|", lw=2))

ax1.text(0.50,-0.07,s=r"\large $\Delta x$",horizontalalignment='center',
        verticalalignment='center',rotation=0)

ax1.text((.71+.792)/2,-0.07,s=r"\large$>\Delta x$",horizontalalignment='center',
        verticalalignment='center',rotation=0)



# Configuracion ejes
plt.ylim(-.1,1)
plt.yticks([])
plt.xticks([])

plt.xlim(0,1)
ax1.axis('off')
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-spatial-3.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-spatial-3.png", dpi=300)
plt.close()