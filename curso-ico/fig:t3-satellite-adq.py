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
x = np.linspace(0, xmax,200)
plt.fill_between(x+np.cos(x+np.pi/4),np.cos(x)/4+ymax/4, np.cos(x)-ymax/2, alpha=0.3)

# Rayleigh
x0 = xmax*0.1
y0 = ymax*0.95
dx = xmax*0.2
dy = -ymax*0.1
plt.annotate("",(x0+dx,y0+dy),(x0,y0), color="k",
            arrowprops=dict(color='k', arrowstyle="-|>",lw=2,alpha=0.1))

plt.plot(x0+dx*1.03,y0+dy*1.03,'.')
x0 = x0+dx*1.08
y0 = y0+dy
xf = (xmax-x0)*0.8+x0
yf = (ymax-y0)*0.8+y0
plt.annotate("",(xf,yf),(x0,y0), color="C0",
            arrowprops=dict(color='C0', arrowstyle="-|>",lw=2))
xR = (x0+xf)/2      
yR = (y0+yf)/2+0      


# Aerosol
x0 = xmax*0.1
y0 = ymax*0.95
dx = xmax*0.15
dy = -ymax*0.4
plt.annotate("",(x0+dx,y0+dy),(x0,y0), color="k",
            arrowprops=dict(color='k', arrowstyle="-|>",lw=2,alpha=0.1))

plt.plot(x0+dx*1.03,y0+dy*1.03,'oC0')
x0 = x0+dx*1.08
y0 = y0+dy
xf = (xmax-x0)*0.82+x0
yf = (ymax-y0)*0.82+y0
plt.annotate("",(xf,yf),(x0,y0), color="C0",
            arrowprops=dict(color='C0', arrowstyle="-|>",lw=2))

plt.text((x0+xf)/2, (y0+yf)/2+0., r"\Large $L_a$", bbox=dict(facecolor='white', edgecolor='none', pad=1.5,boxstyle='round,pad=0.1'),
        horizontalalignment='center', verticalalignment='center')

# Glint
x0 = xmax*0.1
y0 = ymax*0.95
dx = xmax*0.17
dy = -ymax*0.7
plt.annotate("",(x0+dx,y0+dy),(x0,y0), color="k", 
            arrowprops=dict(color='k', arrowstyle="-|>",lw=2,alpha=0.1))

x0 = x0+dx-0.15
y0 = y0+dy+0.1
xf = (xmax-x0)*0.82+x0
yf = (ymax-y0)*0.87+y0
plt.annotate("",(xf,yf),(x0,y0), color="C3",
            arrowprops=dict(color='C3', arrowstyle="-|>",lw=2))

plt.text((x0+xf)/2, (y0+yf)/2+0., r"\Large $TL_g$, $tL_{wc}$" , bbox=dict(facecolor='white', edgecolor='none', pad=1.5,boxstyle='round,pad=0.1'),
        horizontalalignment='center', verticalalignment='center')



# Aerosol + Rayleigh
x0 = xmax*0.1
y0 = ymax*0.95

dx = xmax*0.15+0.2
dy = -ymax*0.4+0.1

dx2 = xmax*0.2+0.07
dy2 = -ymax*0.2+0.8

plt.annotate("",(x0+dx2,y0+dy2),(x0+dx,y0+dy), color="C0",
            arrowprops=dict(color='C0', arrowstyle="-|>",lw=2, ls=":"))

plt.text((2*x0+dx+dx2)/2, (2*y0+dy+dy2)/2, r"\Large $L_{aR}$", bbox=dict(facecolor='white', edgecolor='none', pad=1.5,boxstyle='round,pad=0.1'),
        horizontalalignment='center', verticalalignment='center')

x0 = x0+dx2*1.1-0.15
y0 = y0+dy2*1.0+0.2
xf = (xmax-x0)*0.8+x0
yf = (ymax-y0)*0.65+y0
plt.annotate("",(xf,yf),(x0,y0), color="C0",
            arrowprops=dict(color='C0', arrowstyle="-|>",lw=2,ls=":"))

plt.text(xR, yR, r"\Large $L_R$", bbox=dict(facecolor='white', edgecolor='none', pad=1.5,boxstyle='round,pad=0.1'),
        horizontalalignment='center', verticalalignment='center')


# Water leaving

x0 = xmax*0.1
y0 = ymax*0.95
xfw = xmax/2-0.7
yfw = 0.3
plt.annotate("",(xfw,yfw),(x0,y0), color="k",
            arrowprops=dict(color='k', arrowstyle="-|>",lw=2,alpha=0.1))

plt.plot(xfw, yfw, "C2o")

x0 = xmax/2-0.7
y0 = 0.3
a = 60*np.pi/180
r = ymax/4/np.sin(a)
plt.annotate("",(x0+r*np.cos(a),y0+r*np.sin(a)),(x0,y0), color="C2",
            arrowprops=dict(color='C2', arrowstyle="-",lw=2))
r = r/np.sqrt(2)


r = r*np.sqrt(2)
x0 = x0+r*np.cos(a)-0.1
y0 = y0+r*np.sin(a)-0.15
a = 50*np.pi/180
r = ymax/2/np.sin(a)

plt.annotate("",(xf+0.2,yf-0.7),(x0,y0),
            arrowprops=dict(color='C2', arrowstyle="-|>", lw=2))


plt.text((x0+xf+0.2)/2, (y0+yf-0.7)/2+0., r"\Large $t L_w$", bbox=dict(facecolor='white', edgecolor='none', pad=1.5,boxstyle='round,pad=0.1'),
        horizontalalignment='center', verticalalignment='center')

# Sun and satellite
x0 = xmax*0.1
y0 = ymax*0.95
plt.text((x0), (y0), r"\Huge \faIcon{sun}",
        horizontalalignment='center', verticalalignment='center')

x0 = xmax*0.9
y0 = ymax*0.95
plt.text((x0), (y0), r"\Huge \faIcon{satellite}", rotation=90,
        horizontalalignment='center', verticalalignment='center')


ax1.axis('off')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t3-satellite-adq.pdf")
plt.savefig("curso-ico/figs/fig:t3-satellite-adq.png", dpi=300)