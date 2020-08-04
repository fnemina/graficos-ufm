import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuro latexify a dos columnas
latexify(fig_width=5, fontawesome=True, siunitx=True)

# FROM OSOAA manual
# Modeling Water Clarity and Light Quality in Oceans
# Rango de 350nm a 700nm
g = 0.069
# Grafico
x = np.linspace(400, 700)
x0 = 440
# Grafico
data = np.loadtxt("data/OSOAA_SEA_EUPH_DEPTH.txt")
chl = data[:,0]
dep = data[:,1]
plt.plot(chl, dep)
#plt.yscale("log")
#plt.yticks([0.001,0.01,0.1,1,10,100], [0.001,0.01,0.1,1,10,100])
plt.xlabel(r"$[chla]$ [\si{\milli\gram\per\cubic\meter}]")
plt.ylabel(r"Profundidad eufótica[\si{\meter}]")
plt.xscale("log")
plt.yscale("log")
plt.xticks([0.01,0.1,1,10],[0.01,0.1,1,10])
plt.xlim([0.01,30])
plt.yticks([10,30,100,300],[10,30,100,300])
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-depth.pdf")
plt.savefig("curso-ico/figs/fig:t2-depth.png", dpi=300)
plt.close()

data = np.loadtxt("data/OSOAA_SEA_EUPH_DEPTH.txt")
chl = data[:,0]
dep = data[:,1]
z = np.logspace(-2.2,2.5,200)
for i in range(0,len(chl),3):
    tau = np.log(0.01)/dep[i]
    plt.plot(100*np.exp(tau*z),z, label=f"{chl[i]}"+r"\si{\milli\gram\per\cubic\meter}")
plt.yscale("log")
plt.gca().invert_yaxis()
plt.yticks([0.01,0.1,1,10,100], 
           [r"\SI{1}{\centi\meter}",r"\SI{10}{\centi\meter}",
           r"\SI{1}{\meter}",r"\SI{10}{\meter}",r"\SI{100}{\meter}"])
plt.xticks([0,20,40,60,80,100], ["0\%","20\%","40\%","60\%","80\%","100\%"])
plt.xlabel(r"Porcentaje de irradiancia [\si{\percent}]")
plt.ylabel(r"Profundidad[\si{\meter}]")
plt.legend()
plt.tight_layout()
plt.savefig("curso-ico/figs/fig:t2-lightdepth.pdf")
plt.savefig("curso-ico/figs/fig:t2-lightdepth.png", dpi=300)
plt.close()
