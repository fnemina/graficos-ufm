import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.shape_base import column_stack
from latexify import latexify
from matplotlib import patches
import pyOSOAA
from tqdm import tqdm


fondos = {1:"Negro", 2:"Arena clara",
          3:"Algas verdes",
          4:"Algas marrones",
          5:"Algas rojas"}
# Configuro latexify a dos columnas
latexify(fig_width=7, fontawesome=True, siunitx=True)

profundidad = 30
# We configure simulation
s = pyOSOAA.OSOAA()

tipos = np.array([1,2,3,4,5])    
R_dict = {}
rho_dict = {}
sun = 0
wl = np.arange(400,701,5)

R_dict_001 = {}
rho_dict_001 = {}
chl = 0.01
for tipo in tqdm(tipos):    
    # We create the pyOSOAA object and define the wavelengths using the SeaWiFS values
    R = []
    rho = []
    for wa in wl:
        s = pyOSOAA.OSOAA(cleanup=True, logfile="/tmp/osoaa.log")
        # We configure a black ocean
        #s = pyOSOAA.osoaahelpers.ConfigureOcean(s, ocean_type="black")
        s.phyto.chl = chl
        s.phyto.SetPrimaryMode()
        s.sea.depth=profundidad
        s.sea.bottype = int(tipo)
        if tipo == 1:
            s.sea.botalb=0
        s.phyto.SetProfilType(s.phyto.Gaussian,0,1,1)
        s.sed.csed=0
        s.sed.SetPrimaryMode()
        # Ocean surface
        s.sea.wind = 0
        # Maritime Shettle and Fenn model
        s.aer.SetModel(model=2, sfmodel=3, rh=90)
        s.aer.aotref = 0
        # Relative azymuth angle
        s.view.phi = 90
        # Sun geometry
        s.ang.thetas = 0
        # We set the ap to zero
        s.view.level = 3
        s.ap.SetMot(0.0003)

        # We run simulation
        s.wa = wa/1e3
        s.run()
        R.append(s.outputs.flux.Eu[27]/s.outputs.flux.Ed[27])
        rho.append(np.interp(0, s.outputs.vsvza.vza, s.outputs.vsvza.I)/np.cos(sun*np.pi/180)/np.exp(-0.0003/np.cos(0*np.pi/180.0)))
    R_dict_001[tipo] = R
    rho_dict_001[tipo] = rho

R_dict_01 = {}
rho_dict_01 = {}
chl = 0.1
for tipo in tqdm(tipos):    
    # We create the pyOSOAA object and define the wavelengths using the SeaWiFS values
    R = []
    rho = []
    for wa in wl:
        s = pyOSOAA.OSOAA(cleanup=True, logfile="/tmp/osoaa.log")
        # We configure a black ocean
        #s = pyOSOAA.osoaahelpers.ConfigureOcean(s, ocean_type="black")
        s.phyto.chl = chl
        s.phyto.SetPrimaryMode()
        s.sea.depth=profundidad
        s.sea.bottype = int(tipo)
        if tipo == 1:
            s.sea.botalb=0
        s.phyto.SetProfilType(s.phyto.Gaussian,0,1,1)
        s.sed.csed=0
        s.sed.SetPrimaryMode()
        # Ocean surface
        s.sea.wind = 0
        # Maritime Shettle and Fenn model
        s.aer.SetModel(model=2, sfmodel=3, rh=90)
        s.aer.aotref = 0
        # Relative azymuth angle
        s.view.phi = 90
        # Sun geometry
        s.ang.thetas = 0
        # We set the ap to zero
        s.view.level = 3
        s.ap.SetMot(0.0003)

        # We run simulation
        s.wa = wa/1e3
        s.run()
        R.append(s.outputs.flux.Eu[27]/s.outputs.flux.Ed[27])
        rho.append(np.interp(0, s.outputs.vsvza.vza, s.outputs.vsvza.I)/np.cos(sun*np.pi/180)/np.exp(-0.0003/np.cos(0*np.pi/180.0)))
    R_dict_01[tipo] = R
    rho_dict_01[tipo] = rho

R_dict_1 = {}
rho_dict_1 = {}
chl = 1
for tipo in tqdm(tipos):    
    # We create the pyOSOAA object and define the wavelengths using the SeaWiFS values
    R = []
    rho = []
    for wa in wl:
        s = pyOSOAA.OSOAA(cleanup=True, logfile="/tmp/osoaa.log")
        # We configure a black ocean
        #s = pyOSOAA.osoaahelpers.ConfigureOcean(s, ocean_type="black")
        s.phyto.chl = chl
        s.phyto.SetPrimaryMode()
        s.sea.depth=profundidad
        s.sea.bottype = int(tipo)
        if tipo == 1:
            s.sea.botalb=0
        s.phyto.SetProfilType(s.phyto.Gaussian,0,1,1)
        s.sed.csed=0
        s.sed.SetPrimaryMode()
        # Ocean surface
        s.sea.wind = 0
        # Maritime Shettle and Fenn model
        s.aer.SetModel(model=2, sfmodel=3, rh=90)
        s.aer.aotref = 0
        # Relative azymuth angle
        s.view.phi = 90
        # Sun geometry
        s.ang.thetas = 0
        # We set the ap to zero
        s.view.level = 3
        s.ap.SetMot(0.0003)

        # We run simulation
        s.wa = wa/1e3
        s.run()
        R.append(s.outputs.flux.Eu[27]/s.outputs.flux.Ed[27])
        rho.append(np.interp(0, s.outputs.vsvza.vza, s.outputs.vsvza.I)/np.cos(sun*np.pi/180)/np.exp(-0.0003/np.cos(0*np.pi/180.0)))
    R_dict_1[tipo] = R
    rho_dict_1[tipo] = rho

R_dict_10 = {}
rho_dict_10 = {}
chl = 10
for tipo in tqdm(tipos):    
    # We create the pyOSOAA object and define the wavelengths using the SeaWiFS values
    R = []
    rho = []
    for wa in wl:
        s = pyOSOAA.OSOAA(cleanup=True, logfile="/tmp/osoaa.log")
        # We configure a black ocean
        #s = pyOSOAA.osoaahelpers.ConfigureOcean(s, ocean_type="black")
        s.phyto.chl = chl
        s.phyto.SetPrimaryMode()
        s.sea.depth=profundidad
        s.sea.bottype = int(tipo)
        if tipo == 1:
            s.sea.botalb=0
        s.phyto.SetProfilType(s.phyto.Gaussian,0,1,1)
        s.sed.csed=0
        s.sed.SetPrimaryMode()
        # Ocean surface
        s.sea.wind = 0
        # Maritime Shettle and Fenn model
        s.aer.SetModel(model=2, sfmodel=3, rh=90)
        s.aer.aotref = 0
        # Relative azymuth angle
        s.view.phi = 90
        # Sun geometry
        s.ang.thetas = 0
        # We set the ap to zero
        s.view.level = 3
        s.ap.SetMot(0.0003)

        # We run simulation
        s.wa = wa/1e3
        s.run()
        R.append(s.outputs.flux.Eu[27]/s.outputs.flux.Ed[27])
        rho.append(np.interp(0, s.outputs.vsvza.vza, s.outputs.vsvza.I)/np.cos(sun*np.pi/180)/np.exp(-0.0003/np.cos(0*np.pi/180.0)))
    R_dict_10[tipo] = R
    rho_dict_10[tipo] = rho

colores = {1:"k", 2:"C1", 3:"C2", 4:"C5", 5:"C3"}
plt.plot()
fig, axs = plt.subplots(2, 2, sharey=True, sharex=True)
for tipo in tipos:
    axs[0, 0].plot(wl, np.array(rho_dict_001[tipo])/np.pi, colores[tipo])
axs[0, 0].set_title(r'\SI{0.01}{\milli\gram\per\cubic\meter}')
for tipo in tipos:
    axs[0, 1].plot(wl, np.array(rho_dict_01[tipo])/np.pi, colores[tipo])
axs[0, 1].set_title(r'\SI{0.1}{\milli\gram\per\cubic\meter}')
for tipo in tipos:
    axs[1, 0].plot(wl, np.array(rho_dict_1[tipo])/np.pi, colores[tipo])
axs[1, 0].set_title(r'\SI{1}{\milli\gram\per\cubic\meter}')

for tipo in tipos:
    if tipo == 2:
        if profundidad<900:
            axs[1, 1].plot([],[],"w",label=f"{profundidad}"+r"\si{\meter}")
        else:
            axs[1, 1].plot([],[],"w",label=r"$\infty$\si{\meter}")
    axs[1, 1].plot(wl, np.array(rho_dict_10[tipo])/np.pi, colores[tipo], label=f"{fondos[tipo]}")
axs[1, 1].set_title(r'\SI{10}{\milli\gram\per\cubic\meter}')

for ax in axs.flat:
    ax.set(xlabel=r"$\lambda$ [\si{\nano\meter}]", ylabel=r"$Rrs$ ", yticks=[0,0.02,0.04], ylim=[-0.003,0.043])
for ax in axs.flat:
    ax.label_outer()

handles, labels = axs[1,1].get_legend_handles_labels()
lgd = fig.legend(handles, labels, loc='upper center', ncol=3, bbox_to_anchor=(0.5, 1.06), borderaxespad=0.)
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t2-fondo-{profundidad}.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t2-fondo-{profundidad}.png", dpi=300,bbox_inches='tight')
plt.close()