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

x0 = 0.5
ax1.text(x0,0.95,s=r"\large 1",horizontalalignment='center',verticalalignment='center',rotation=0)
ax1.text(x0+0.01,0.85,s=r"\Huge\faIcon{satellite}",horizontalalignment='center',verticalalignment='center',rotation=135)
# SWADTH
x = np.linspace(x0,x0+0.28)
y = 3*(x0-x)+0.85
z = 3*(x0-x)+0.85

plt.plot(1-x,y,'k--',alpha=0.3)
plt.plot(x,z,'k--',alpha=0.3)

x0 = 0.75
ax1.text(x0,0.95,s=r"\large 2",horizontalalignment='center',verticalalignment='center',rotation=0)
ax1.text(x0+0.01,0.85,s=r"\Huge\faIcon{satellite}",horizontalalignment='center',verticalalignment='center',rotation=135)
# SWADTH
x = np.linspace(x0,x0+0.28)
y = 3*(x0-x)+0.85
z = 3*(x0-x)+0.85
x = np.linspace(x0,x0+0.28)
plt.plot(2*x0-x,y,'k--',alpha=0.3)
x = np.linspace(x0,x0+0.28)
plt.plot(x,z,'k--',alpha=0.3)

x0 = 0.25
ax1.text(x0,0.95,s=r"\large 2",horizontalalignment='center',verticalalignment='center',rotation=0)
ax1.text(x0+0.01,0.85,s=r"\Huge\faIcon{satellite}",horizontalalignment='center',verticalalignment='center',rotation=135)
# SWADTH
x = np.linspace(x0,x0+0.28)
y = 3*(x0-x)+0.85
z = 3*(x0-x)+0.85
x = np.linspace(x0,x0+0.28)
plt.plot(2*x0-x,y,'k--',alpha=0.3)
x = np.linspace(x0,x0+0.28)
plt.plot(x,z,'k--',alpha=0.3)

for i in range(5):
    dx = np.random.uniform(0.98,1.02)
    dy = np.random.uniform(0.7,1.3)
    a = np.random.uniform(0,180)
    ax1.text(0.5*dx,-0.04*dy,s=r"\small\faIcon{spider}",
            horizontalalignment='center', rotation=a,
            verticalalignment='center_baseline', color="C2", alpha=0.5)



# Configuracion ejes
plt.ylim(-.1,1)
plt.yticks([])
plt.xticks([])

plt.xlim(0,1)
ax1.axis('off')
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-temporal.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-temporal.png", dpi=300)
plt.close()