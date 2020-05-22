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



# Radiance
for ang in [20,40,60,80,100]:
    x0 = 2.3*xmax/4
    y0 = 1.3*ymax/4
    a = ang*np.pi/180
    x0 = x0
    y0 = y0
    r = -ymax*((ang-10)*(ang-110))/4000
    plt.annotate("",(x0+r*np.cos(a),y0+r*np.sin(a)),(x0,y0),
                arrowprops=dict(color='C2', arrowstyle="-",lw=2))
    r = r/np.sqrt(2)
    plt.annotate("",(x0+r*np.cos(a),y0+r*np.sin(a)),(x0,y0),
                arrowprops=dict(color='C2', arrowstyle="-|>, head_width=0.3,head_length=1",
                lw=2))
# Patches
plt.annotate("",(x0,y0),(x0*1.01,y0*1.01),
            arrowprops=dict(color='white', arrowstyle="-",
            lw=20))


# Water
x = np.linspace(0, xmax,200)
plt.fill_between(x+np.cos(x+np.pi/4),np.cos(x)/4+ymax/4, np.cos(x)-ymax/2, alpha=0.3)


# Irradiance
x0 = xmax/4
y0 = 5*ymax/6
a = -55*np.pi/180
r = -ymax/2/np.sin(a)
plt.annotate("",(x0+r*np.cos(a),y0+r*np.sin(a)),(x0,y0), color="C3",
            arrowprops=dict(color='C3', arrowstyle="-",lw=2))
r = r/np.sqrt(2)
plt.annotate("",(x0+r*np.cos(a),y0+r*np.sin(a)),(x0,y0), color="C3",
            arrowprops=dict(color='C3', arrowstyle="-|>, head_width=0.3,head_length=1",
            lw=2))

x0 = xmax/4+1
y0 = 5*ymax/6
a = -55*np.pi/180
r = -ymax/2/np.sin(a)
plt.annotate("",(x0+r*np.cos(a),y0+r*np.sin(a)),(x0,y0), color="C3",
            arrowprops=dict(color='C3', arrowstyle="-",lw=2))
r = r/np.sqrt(2)
plt.annotate("",(x0+r*np.cos(a),y0+r*np.sin(a)),(x0,y0), color="C3",
            arrowprops=dict(color='C3', arrowstyle="-|>, head_width=0.3,head_length=1",
            lw=2))

x0 = xmax/4-1
y0 = 5*ymax/6
a = -55*np.pi/180
r = -ymax/2/np.sin(a)
plt.annotate("",(x0+r*np.cos(a),y0+r*np.sin(a)),(x0,y0), color="C3",
            arrowprops=dict(color='C3', arrowstyle="-",lw=2))
r = r/np.sqrt(2)
plt.annotate("",(x0+r*np.cos(a),y0+r*np.sin(a)),(x0,y0), color="C3",
            arrowprops=dict(color='C3', arrowstyle="-|>, head_width=0.3,head_length=1",
            lw=2))

# Texto
ax1.text(xmax/2-2,2*ymax/3,s=r"\large$E_d^{0^+}$",horizontalalignment='right', verticalalignment='center_baseline')
ax1.text(xmax/2+7.5,2*ymax/3,s=r"\large$E_u^{0^+}$",horizontalalignment='right', verticalalignment='center_baseline')
ax1.text(xmax-1,ymax/4+0.5,s=r"\large$0^+$",horizontalalignment='right', verticalalignment='center_baseline')
ax1.text(xmax-1,ymax/4-0.75,s=r"\large$0^-$",horizontalalignment='right', verticalalignment='center_baseline')


ax1.axis('off')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t1-reflectance0.pdf")
plt.savefig("curso-ico/figs/fig:t1-reflectance0.png", dpi=300)