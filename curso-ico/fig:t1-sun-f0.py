import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(columns=2, fontawesome=True, siunitx=True)

# Grafico
fig = plt.figure()
ax1 = fig.add_subplot(111)
data = np.loadtxt("data/f0.txt", comments=["!","/"])
plt.plot(data[:,0],data[:,1], label="Iluminación solar")
plt.xlabel(r"$\lambda$[\si{\nano\meter}]")
plt.xticks(np.arange(250,2500,250))
plt.ylabel(r"$F_0(\lambda)$[\si{\micro\watt\per\centi\meter\squared\per\nano\meter}]")
plt.legend(fancybox=True)
i = 0

# # VISIBLE
i = 1
xmin=380
xmax=740
ax1.annotate('', xy=(xmin, 50),xytext=(xmax, 50),
            arrowprops=dict(facecolor='black', arrowstyle="|-|"))
ax1.text((xmax+xmin)/2,55,s=r"Visible",
        horizontalalignment='center', verticalalignment='center')

# # UV
i = 2
xmin=150
xmax=380
ax1.annotate('', xy=(xmin, 50),xytext=(xmax, 50),
            arrowprops=dict(facecolor='black', arrowstyle="->"))
ax1.text((xmax+xmin)/2,55,s=r"UV",bbox=dict(facecolor='white', edgecolor='none', pad=1.5,boxstyle='round,pad=0.1'),
        horizontalalignment='center', verticalalignment='center')
xmin=150
xmax=375
ax1.annotate('', xy=(xmax, 50),xytext=(xmax+1, 50),
            arrowprops=dict(facecolor='black', arrowstyle="|-|"))

# # IR
i = 3
xmin=745
xmax=2300
ax1.annotate('', xy=(xmin, 50),xytext=(xmin+1, 50),
            arrowprops=dict(facecolor='black', arrowstyle="|-|"))
xmin=740
xmax=2450
ax1.annotate('', xy=(xmin, 50),xytext=(xmax, 50),
            arrowprops=dict(facecolor='black', arrowstyle="<-"))
ax1.text((xmax+xmin)/2,55,s=r"IR",
        horizontalalignment='center', verticalalignment='center')

# # NIR
i = 4
xmin=740
xmax=1400
ax1.annotate('', xy=(xmin, 30),xytext=(xmax, 30),
            arrowprops=dict(facecolor='black', arrowstyle="|-|"))
ax1.text((xmax+xmin)/2,35,s=r"NIR",
        horizontalalignment='center', verticalalignment='center')


# # SWIR
i = 5
xmin=1405
xmax=2300
ax1.annotate('', xy=(xmin, 30),xytext=(xmin+1, 30),
            arrowprops=dict(facecolor='black', arrowstyle="|-|"))
xmin=1400
xmax=2450
ax1.annotate('', xy=(xmin, 30),xytext=(xmax, 30),
            arrowprops=dict(facecolor='black', arrowstyle="<-"))
ax1.text((xmax+xmin)/2,35,s=r"SWIR",
        horizontalalignment='center', verticalalignment='center')


# # OC
# i = 6
# xmin=350
# xmax=2300
# ax1.annotate('', xy=(xmin, 10),xytext=(xmax, 10),
#             arrowprops=dict(facecolor='black', arrowstyle="|-|"))
# ax1.text((xmax+xmin)/2,15,s=r"Color del océano",
#         horizontalalignment='center', verticalalignment='center')

# # OC division
i = 7
xmin=400
xmax=700
ax1.annotate('', xy=(xmin, 10),xytext=(xmax, 10),
            arrowprops=dict(facecolor='C2',color="C2", arrowstyle="|-|"))
ax1.text((xmax+xmin)/2,15,s=r"Productos",
        horizontalalignment='center', verticalalignment='center')

xmin=350
xmax=400
ax1.annotate('', xy=(xmin, 10),xytext=(xmax, 10),color="C0",
            arrowprops=dict(facecolor='C0',color="C1", arrowstyle="|-|"))
ax1.text((xmax+xmin)/2,15,s=r"",
        horizontalalignment='center', verticalalignment='center')

xmin=700
xmax=2300
ax1.annotate('', xy=(xmin, 10),xytext=(xmax, 10),
            arrowprops=dict(facecolor='C0',color="C1", arrowstyle="|-|"))

xmin=350
ax1.text((xmax+xmin)/2,15,s=r"Corrección atmosférica",
        horizontalalignment='center', verticalalignment='center')

plt.xlim(100,2500)

plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t1-sun-f0-{i}.pdf")
plt.savefig(f"curso-ico/figs/fig:t1-sun-f0-{i}.png", dpi=300)
plt.close()