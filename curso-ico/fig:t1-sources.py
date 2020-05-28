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
ax1.set_xlim(0,xmax)
ax1.set_ylim(0,ymax)

# Water
x = np.linspace(0, xmax/2,200)
plt.xlim(0,xmax/2)
plt.fill_between(x+np.cos(np.pi/4),-0.01*(x-xmax/4)**2+1*ymax, 0, alpha=0.1)
plt.fill_between(x+np.cos(x+np.pi/4),np.cos(x)/4+ymax/4, np.cos(x)-ymax/2, color="C0",linewidth=0.0,alpha=0.25)

# Icons
alpha = 1

ax1.text(0.1*xmax/2,2.5*ymax/2,s=r"\Huge\faIcon{sun}",
            horizontalalignment='center', 
            verticalalignment='center_baseline', alpha=alpha)

plt.annotate("",(0.55*xmax/2/1.1,0.5*ymax/2),(0.125*xmax/2,2.325*ymax/2),
            arrowprops=dict(color='k', arrowstyle="-|>, head_width=0.3,head_length=1",
            lw=2, alpha=alpha))

for i in range(5):
    dx = np.random.uniform(0.98,1.02)
    dy = np.random.uniform(0.7,1.3)
    a = np.random.uniform(0,180)
    ax1.text(0.55*xmax/2*dx,0.25*ymax/2*dy,s=r"\small\faIcon{spider}",
            horizontalalignment='center', rotation=a,
            verticalalignment='center_baseline', color="C2", alpha=alpha)

plt.annotate("",(0.55*xmax/2*1.1,0.5*ymax/2),(1.*xmax/2/1.03,2.5*ymax/2/1.1),
            arrowprops=dict(color='k', arrowstyle="<|-, head_width=0.3,head_length=1",
            lw=2, alpha=alpha))

ax1.text(1.*xmax/2,2.5*ymax/2,s=r"\Huge\faIcon{satellite}",
            rotation=+73,
            horizontalalignment='center', 
            verticalalignment='center_baseline', alpha=alpha)


ax1.axis('off')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-sources-sun.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-sources-sun.png", dpi=300)
plt.close()


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
ax1.set_xlim(0,xmax)
ax1.set_ylim(0,ymax)

# Water
x = np.linspace(0, xmax/2,200)
plt.xlim(0,xmax/2)
plt.fill_between(x+np.cos(np.pi/4),-0.01*(x-xmax/4)**2+1*ymax, 0, alpha=0.1)
plt.fill_between(x+np.cos(x+np.pi/4),np.cos(x)/4+ymax/4, np.cos(x)-ymax/2, color="C0",linewidth=0.0,alpha=0.25)

# Icons
alpha = 1

for i in range(5):
    dx = np.random.uniform(0.98,1.02)
    dy = np.random.uniform(0.7,1.3)
    a = np.random.uniform(0,180)
    ax1.text(0.55*xmax/2*dx,0.25*ymax/2*dy,s=r"\small\faIcon{spider}",
            horizontalalignment='center', rotation=a,
            verticalalignment='center_baseline', color="C2", alpha=alpha)

plt.annotate("",(0.55*xmax/2*1.1,0.5*ymax/2),(1.*xmax/2/1.03,2.5*ymax/2/1.1),
            arrowprops=dict(color='k', arrowstyle="<|-, head_width=0.3,head_length=1",
            lw=2, alpha=alpha))

plt.annotate("",(0.55*xmax/2*1.1-0.125,0.5*ymax/2+0.25),(1.*xmax/2/1.03-0.125,2.5*ymax/2/1.1+0.25),
            arrowprops=dict(color='k', arrowstyle="-|>, head_width=0.3,head_length=1",
            lw=2, alpha=alpha))

ax1.text(1.*xmax/2,2.5*ymax/2,s=r"\Huge\faIcon{satellite}",
            rotation=+73,
            horizontalalignment='center', 
            verticalalignment='center_baseline', alpha=alpha)


ax1.axis('off')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-sources-sat.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-sources-sat.png", dpi=300)
plt.close()


# Grafico
fig = plt.figure(figsize=(6.9,3))
ax1 = fig.add_subplot(111)
xmax = 8*np.pi
ymax = xmax/((6.9/3))
ax1.set_xlim(0,xmax)
ax1.set_ylim(0,ymax)

# Water
x = np.linspace(0, xmax/2,200)
plt.xlim(0,xmax/2)
plt.fill_between(x+np.cos(np.pi/4),-0.01*(x-xmax/4)**2+1*ymax, 0, alpha=0.1)
plt.fill_between(x+np.cos(x+np.pi/4),np.cos(x)/4+ymax/4, np.cos(x)-ymax/2, color="C0",linewidth=0.0,alpha=0.25)

# Icons
alpha = 1

ax1.text(0.1*xmax/2,2.5*ymax/2,s=r"\Huge\faIcon{moon}",
            horizontalalignment='center', 
            verticalalignment='center_baseline', alpha=alpha)



for i in range(5):
    dx = np.random.uniform(0.98,1.02)
    dy = np.random.uniform(0.7,1.3)
    a = np.random.uniform(0,180)
    ax1.text(0.55*xmax/2*dx,0.25*ymax/2*dy,s=r"\small\faIcon{spider}",
            horizontalalignment='center', rotation=a,
            verticalalignment='center_baseline', color="C2", alpha=alpha)

plt.annotate("",(0.55*xmax/2*1.1,0.5*ymax/2),(1.*xmax/2/1.03,2.5*ymax/2/1.1),
            arrowprops=dict(color='k', arrowstyle="<|-, head_width=0.3,head_length=1",
            lw=2, alpha=alpha))

ax1.text(1.*xmax/2,2.5*ymax/2,s=r"\Huge\faIcon{satellite}",
            rotation=+73,
            horizontalalignment='center', 
            verticalalignment='center_baseline', alpha=alpha)


ax1.axis('off')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-sources-water.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-sources-water.png", dpi=300)
plt.close()