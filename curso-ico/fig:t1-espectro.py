import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(columns=2, fontawesome=True)

# Grafico
fig = plt.figure()
ax1 = fig.add_subplot(111)
x = np.logspace(-13,4,10000)
ticks = np.arange(-12,2,1)
y = np.sin(np.log(x/10)**2/np.log(10))*0.10+0.75
plt.plot(x,y,'black',alpha=0.3)

# Regiones del espectro
plt.axvline(x=10**-11,ymin=-.1,ymax=0.41)
plt.axvline(x=10**-9,ymin=-.1,ymax=0.41)
#plt.axvline(x=400*10**-9,ymin=-.1,ymax=0.41)
#plt.axvline(x=780*10**-9,ymin=-.1,ymax=0.41)
plt.axvline(x=10**-4,ymin=-.1,ymax=0.41)
plt.axvline(x=10**-1,ymin=-.1,ymax=0.41)

# parches
ax1.axes.add_patch(
    patches.Rectangle(
        (0.4*10**-6, 0.2),   # (x,y)
        20*10**-9,          # width
        0.3,          # height
        facecolor="violet",
        edgecolor="violet"
    )
)
ax1.axes.add_patch(
    patches.Rectangle(
        (0.42*10**-6, 0.2),   # (x,y)
        20*10**-9,          # width
        0.3,          # height
        facecolor="indigo",
        edgecolor="indigo"
    )
)
ax1.axes.add_patch(
    patches.Rectangle(
        (0.44*10**-6, 0.2),   # (x,y)
        50*10**-9,          # width
        0.3,          # height
        facecolor="blue",
        edgecolor="blue"
    )
)
ax1.axes.add_patch(
    patches.Rectangle(
        (0.49*10**-6, 0.2),   # (x,y)
        80*10**-9,          # width
        0.3,          # height
        facecolor="green",
        edgecolor="green"
    )
)
ax1.axes.add_patch(
    patches.Rectangle(
        (0.57*10**-6, 0.2),   # (x,y)
        15*10**-9,          # width
        0.3,          # height
        facecolor="yellow",
        edgecolor="yellow"
    )
)
ax1.axes.add_patch(
    patches.Rectangle(
        (0.585*10**-6, 0.2),   # (x,y)
        35*10**-9,          # width
        0.3,          # height
        facecolor="orange",
        edgecolor="orange"
    )
)
ax1.axes.add_patch(
    patches.Rectangle(
        (0.62*10**-6, 0.2),   # (x,y)
        160*10**-9,          # width
        0.3,          # height
        facecolor="red",
        edgecolor="red"
    )
)

# Texto en los ejes
ax1.text(10**-12,0.32,s="Rayos gama",horizontalalignment='center')
ax1.text(10**-10,0.32,s="Rayos X",horizontalalignment='center')
ax1.text(10**-7.699,0.32,s="Ultravioleta",horizontalalignment='center')
ax1.text(10**-6.253,0.17,s="Visible",horizontalalignment='center')
ax1.text(10**-5.054,0.32,s="Infrarrojo",horizontalalignment='center')
ax1.text(10**-2.5,0.32,s="Microondas",horizontalalignment='center')
ax1.text(10**-.5,0.32,s="Radio\nTV",horizontalalignment='center',verticalalignment='center')

# Ventanas atmosfericas
data = np.loadtxt("data/atm_w.csv",delimiter=',')
xo = data[:,0]
yo = data[:,1]
plt.fill_between(xo,yo*0.5+0.5,0.5,facecolor='black',alpha=0.1)


# Configuracion ejes
plt.ylim(0.15,1)
plt.yticks([])
plt.xscale('log')

plt.xlim(10**-13,1)
plt.xlabel("Longitud de onda [m]")

ticks = np.array([3.,6.,9.,12.,15.,18.,21.])
xticks = 299792458.0/10.**ticks
ax2 = ax1.twiny()
ax2.set_xlim(10**-13,1)
ax2.set_xscale('log')
ax2.set_xticks(xticks)
ax2.set_xticklabels([r"$10^3$",r"$10^6$",r"$10^9$",r"$10^{12}$",r"$10^{15}$",r"$10^{18}$",r"$10^{21}$"])
ax2.set_xlabel("Frecuencia [Hz]")
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t1-espectrum.pdf")
plt.savefig("curso-ico/figs/fig:t1-espectrum.png", dpi=300)