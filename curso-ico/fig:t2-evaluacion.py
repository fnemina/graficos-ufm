name = "fig:evalucion"

import numpy as np
import matplotlib.pyplot as plt
from latexify import latexify
from matplotlib import patches

# Configuracion
# 
# Poner acá tantas curvas como quieras
# Tiene que ser [chl, nap, cdom]
options = {"A":[0.1,0,0],
           "B":[1.0,0,0],
           "C":[10.,0,0]}

chl = 0.01
cdom = 0.0
nap = 0

# Configuro latexify a dos columnas
latexify(fig_width=5, fontawesome=True, siunitx=True)
fig = plt.figure(figsize=(6,2.25*1.5))
for key in options.keys():
    chl = options[key][0]
    nap = options[key][1]
    cdom= options[key][2]
    # FROM OSOAA manual
    # 4.3.3.2 Sea molecule profile
    g = 0.069
    x = np.linspace(400, 700)
    # scattering
    bbwater = 0.00288*(x/500)**(-4.32)
    bbchla = 0.03*(550/x)*chl**(0.62)
    bbnap = 0.604*nap**(0.766)*(x/550)**(-0.8)
    bb = bbwater+bbchla+bbnap
    # absorption
    dataw = np.loadtxt("data/OSOAA_SEA_MOL_COEFFS_JUNE_2013.txt")
    datac = np.loadtxt("data/OSOAA_SEA_PHYT_COEFFS.txt")
    AP = np.interp(x, datac[:,0], datac[:,1])
    EP = np.interp(x, datac[:,0], datac[:,2])
    awater = np.interp(x, dataw[:,0], dataw[:,1])
    achla = AP*chl**EP
    acdom = cdom*np.exp(-0.02*(x-440))
    anap = 0.095*nap**(0.626)*np.exp(-0.06*(x-440))
    a = awater+achla+acdom+anap

    plt.plot(x, g*bb/(a+bb), label=r"..................")

plt.ylabel(r"$R$ ")
plt.xlabel(r"$\lambda$ [\si{\nano\meter}]")
legend=plt.legend(fontsize=12, loc="upper right")
plt.setp(legend.get_texts(), color='w')
plt.tight_layout()
plt.savefig(name+".png", dpi=300)
plt.close()