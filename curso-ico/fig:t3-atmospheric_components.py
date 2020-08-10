import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.shape_base import column_stack
from latexify import latexify
from matplotlib import patches
import Py6S
import pyOSOAA
from tqdm import tqdm

modelos = {1 : "Modelo troposférico - Shettle y Fenn",
          2 : "Modelo urbano - Shettle y Fenn",
          3 : "Modelo maritimo - Shettle y Fenn",
          4 : "Modelo costero - Shettle y Fenn"}

fondos = {1:"Negro", 2:"Arena clara",
          3:"Algas verdes",
          4:"Algas marrones",
          5:"Algas rojas"}
# Configuro latexify a dos columnas
latexify(columns=2, fontawesome=True, siunitx=True)
#latexify(fig_width=7, fontawesome=True, siunitx=True)

profundidad = 100
# We configure simulation
s = pyOSOAA.OSOAA()

wl = np.arange(400,1600,10)

sun = 35
view = 0
phi = 90
aot = 0.1
chl = 1
wind = 5

# Transmittance
s = Py6S.SixS()
s.geometry = Py6S.Geometry.User()
s.geometry.solar_a = phi
s.geometry.view_a = 0
s.geometry.solar_z = sun
s.geometry.view_z = view

s.atmos_profile = Py6S.AtmosProfile.UserWaterAndOzone(3.6,0.9)

wl0, T = Py6S.SixSHelpers.Wavelengths.run_whole_range(s, output_name="total_gaseous_transmittance", verbose=False) 
T = np.interp(wl, wl0*1e3, T)
wl0, Tw = Py6S.SixSHelpers.Wavelengths.run_whole_range(s, output_name="transmittance_water.total", verbose=False) 
Tw = np.interp(wl, wl0*1e3, Tw)
wl0, To3 = Py6S.SixSHelpers.Wavelengths.run_whole_range(s, output_name="transmittance_ozone.total", verbose=False) 
To3 = np.interp(wl, wl0*1e3, To3)
wl0, To2 = Py6S.SixSHelpers.Wavelengths.run_whole_range(s, output_name="transmittance_oxygen.total", verbose=False) 
To2 = np.interp(wl, wl0*1e3, To2)
wl0, Tco2 = Py6S.SixSHelpers.Wavelengths.run_whole_range(s, output_name="transmittance_co2.total", verbose=False) 
Tco2 = np.interp(wl, wl0*1e3, Tco2)


fig, ax1 = plt.subplots()
plt.plot(wl, Tw, label=r"$\text{H}_2\text{O}$")
plt.plot(wl, To2, label=r"$\text{O}_2$")
plt.plot(wl, To3, label=r"$\text{O}_3$")
plt.plot(wl, Tco2, label=r"$\text{C}\text{O}_2$")
plt.legend()

plt.xlabel(r"Longitud de onda [\si{\nano\meter}]")
plt.ylabel(r"Transmitancia")
plt.legend()
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-transmitancias.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-transmitancias.png", dpi=300,bbox_inches='tight')
plt.close()


rho_gli = np.array([])
rho_ray = np.array([])
rho_aer = np.array([])
rho_sur = np.array([])
rho_chl = np.array([])
rho_toa = np.array([])
tau_tot = np.array([])
tau_ray = np.array([])

rho_toa_chl = {}
rho_sur_chl = {}
for chl in [0.1,1,10]:
    rho_gli = np.array([])
    rho_ray = np.array([])
    rho_aer = np.array([])
    rho_sur = np.array([])
    rho_chl = np.array([])
    rho_toa = np.array([])
    tau_tot = np.array([])
    tau_ray = np.array([])

    for wa in tqdm(wl):
        s = pyOSOAA.OSOAA(logfile="/tmp/osoaa_ufm.log")
        # We configure a black ocean
        s = pyOSOAA.osoaahelpers.ConfigureOcean(s, ocean_type="black")
        s.sea.depth=profundidad
        s.sea.botalb=0
        
        s.sed.csed=0
        s.sed.SetPrimaryMode()
        # Ocean surface
        s.sea.wind = wind
        # Maritime Shettle and Fenn model
        s.aer.SetModel(model=2, sfmodel=3, rh=90)
        s.aer.aotref = 0.
        # Relative azymuth angle
        s.view.phi = phi
        # Sun geometry
        s.ang.thetas = sun
        # We set the ap to zero
        s.view.level = 3
        s.ap.SetMot(0.0003)

        # We run simulation
        s.wa = wa/1e3
        s.run()
        rho_gli_tmp = np.interp(view, s.outputs.vsvza.vza, s.outputs.vsvza.I)/np.cos(sun*np.pi/180)

        # Rayleigh
        s.ap.SetPressure()
        s.view.level = 1
        s.aer.aotref = 0
        s.run()
        rho_ray_tmp = np.interp(view, s.outputs.vsvza.vza, s.outputs.vsvza.I)/np.cos(sun*np.pi/180)
        tau_ray = np.append(tau_ray, s.outputs.profileatm.tau[-1])

        # Aerosol
        s.aer.aotref = aot
        s.run()
        rho_aer_tmp = np.interp(view, s.outputs.vsvza.vza, s.outputs.vsvza.I)/np.cos(sun*np.pi/180)
        tau_tot = np.append(tau_tot, s.outputs.profileatm.tau[-1])
        
        
        rho_gli = np.append(rho_gli, rho_gli_tmp*np.exp(-tau_tot[-1]*(1/np.cos(sun*np.pi/180)+1/np.cos(view*np.pi/180))))
        rho_ray = np.append(rho_ray, rho_ray_tmp - rho_gli[-1])
        rho_aer = np.append(rho_aer, rho_aer_tmp - rho_gli[-1] - rho_ray[-1])

        # chl    
        s = pyOSOAA.OSOAA(logfile="/tmp/osoaa_ufm.log")
        s.wa = wa/1e3
        s.sea.depth=profundidad
        s.sea.botalb=0
        s.phyto.chl = chl
        
        s.sed.csed=0
        s.sed.SetPrimaryMode()
        # Ocean surface
        s.sea.wind = 0
        # Maritime Shettle and Fenn model
        s.aer.SetModel(model=2, sfmodel=3, rh=90)
        s.aer.aotref = 0.
        # Relative azymuth angle
        s.view.phi = phi
        # Sun geometry
        s.ang.thetas = sun
        # We set the ap to zero
        s.view.level = 3
        s.ap.SetMot(0.0003)
        s.run()
        rho_chl_tmp = np.interp(view, s.outputs.vsvza.vza, s.outputs.vsvza.I)/np.cos(sun*np.pi/180)
        rho_chl = np.append(rho_chl, rho_chl_tmp)

        # toa
        s = pyOSOAA.OSOAA(logfile="/tmp/osoaa_ufm.log")
        s.wa = wa/1e3
        s.sea.depth=profundidad
        s.sea.botalb=0
        s.phyto.chl = chl
        
        s.sed.csed=0
        s.sed.SetPrimaryMode()
        # Ocean surface
        s.sea.wind = wind
        # Maritime Shettle and Fenn model
        s.aer.SetModel(model=2, sfmodel=3, rh=90)
        s.aer.aotref = aot
        # Relative azymuth angle
        s.view.phi = phi
        # Sun geometry
        s.ang.thetas = sun
        # We set the ap to zero
        s.view.level = 1
        s.run()
        rho_toa_tmp = np.interp(view, s.outputs.vsvza.vza, s.outputs.vsvza.I)/np.cos(sun*np.pi/180)
        rho_toa = np.append(rho_toa, rho_toa_tmp)

    rho_toa_chl[chl] = rho_toa
    rho_sur_chl[chl] = rho_chl

fig, ax1 = plt.subplots()
t = np.exp(-tau_ray/2*(1+1/np.cos(view*np.pi/180)))
ax1.plot(wl, rho_toa*T, "k", label=r"$\rho_{toa}$ con absorción gaseoa", alpha=0.4)
ax1.plot(wl, rho_toa, "k", label=r"$\rho_{toa}$ sin absorción gaseoa")
ax1.plot(wl, rho_ray+rho_aer, "C0", label=r"$\rho_{p}$ debida a la atmósfera")
#ax1.plot(wl, rho_aer, "C0-.")
ax1.plot(wl, rho_gli, "C3", label=r"$T \rho_{s}$ debida a la superficie")
ax1.plot(wl, rho_chl*t, "C2", label=r"$t \rho_{w}$ debida al agua")

#ax2 = ax1.twinx() 
#ax2.plot(wl, T, "k", alpha=0.5)
plt.xlabel(r"Longitud de onda [\si{\nano\meter}]")
plt.ylabel(r"$\rho$")
plt.legend()
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_components.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_components.png", dpi=300,bbox_inches='tight')
plt.close()

fig, ax1 = plt.subplots()
t = np.exp(-tau_ray/2*(1+1/np.cos(view*np.pi/180)))
ax1.plot(wl, (rho_ray+rho_aer)/rho_toa*100, "C0", label=r"$\rho_{p}$ en porcentaje de la atmósfera")
#ax1.plot(wl, rho_aer, "C0-.")
ax1.plot(wl, rho_gli/rho_toa*100, "C3", label=r"$T \rho_{s}$ en porcentaje de la superficie")
ax1.plot(wl, rho_chl*t/rho_toa*100, "C2", label=r"$t \rho_{w}$ en porcentaje del agua")

#ax2 = ax1.twinx() 
#ax2.plot(wl, T, "k", alpha=0.5)
plt.xlabel(r"Longitud de onda [\si{\nano\meter}]")
plt.ylabel(r"$\rho$")
plt.legend()
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_percent.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_percent.png", dpi=300,bbox_inches='tight')
plt.close()


fig, ax1 = plt.subplots()
t = np.exp(-tau_ray/2*(1+1/np.cos(view*np.pi/180)))
lines = ["C0","C1","C2"]
i = 0
ax1.plot([],[],"k",label="Reflectancia en a tope de la atmósfera")
ax1.plot([],[],"k-.",label="Reflectancia a tope del océano")
for chl in rho_toa_chl.keys():
    ax1.plot(wl, rho_toa_chl[chl]*T,lines[i]+"-", alpha=0.1)
    ax1.plot(wl, rho_sur_chl[chl], lines[i]+"-.")
    plt.plot([],[], lines[i]+"s",label=f"[chla]={chl}"+r"\si{\milli\gram\per\cubic\meter}")
    i = i+1

#ax2 = ax1.twinx() 
#ax2.plot(wl, T, "k", alpha=0.5)
plt.xlabel(r"Longitud de onda [\si{\nano\meter}]")
plt.ylabel(r"$\rho$")
plt.legend()
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-comp_sur.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-comp_sur.png", dpi=300,bbox_inches='tight')
plt.close()

fig, ax1 = plt.subplots()
t = np.exp(-tau_ray/2*(1+1/np.cos(view*np.pi/180)))
lines = ["C0","C1","C2"]
i = 0
ax1.plot([],[],"k",label="Reflectancia en a tope de la atmósfera")
ax1.plot([],[],"k-.",label="Reflectancia a tope del océano")
for chl in rho_toa_chl.keys():
    ax1.plot(wl, rho_toa_chl[chl]*T,lines[i]+"-")
    ax1.plot(wl, rho_sur_chl[chl], lines[i]+"-.")
    plt.plot([],[], lines[i]+"s",label=f"[chla]={chl}"+r"\si{\milli\gram\per\cubic\meter}")
    i = i+1

#ax2 = ax1.twinx() 
#ax2.plot(wl, T, "k", alpha=0.5)
plt.xlabel(r"Longitud de onda [\si{\nano\meter}]")
plt.ylabel(r"$\rho$")
plt.legend()
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-comp_toa.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-comp_toa.png", dpi=300,bbox_inches='tight')
plt.close()

plt.plot(wl, rho_ray, label="Scattering de Rayleigh")

#ax2 = ax1.twinx() 
#ax2.plot(wl, T, "k", alpha=0.5)
plt.xlabel(r"Longitud de onda [\si{\nano\meter}]")
plt.ylabel(r"$\rho$")
plt.legend()
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-rayleigh.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-rayleigh.png", dpi=300,bbox_inches='tight')
plt.close()

wl = np.arange(400,1600,100)

rho_aer = {}
for model in modelos.keys():
    rho_aer_tmp = np.array([])
    for wa in tqdm(wl):
        s = pyOSOAA.OSOAA(logfile="/tmp/osoaa_ufm.log")
        # We configure a black ocean
        s = pyOSOAA.osoaahelpers.ConfigureOcean(s, ocean_type="black")
        # Ocean surface
        s.sea.wind = 0
        # Maritime Shettle and Fenn model
        s.aer.SetModel(model=model, sfmodel=3, rh=90)
        s.aer.aotref = 0.1
        # Relative azymuth angle
        s.view.phi = phi
        # Sun geometry
        s.ang.thetas = sun
        # We set the ap to zero
        s.view.level = 1
        s.ap.SetMot(0)

        # We run simulation
        s.wa = wa/1e3
        s.run()
        rho_tmp = np.interp(view, s.outputs.vsvza.vza, s.outputs.vsvza.I)/np.cos(sun*np.pi/180)
        rho_aer_tmp = np.append(rho_aer_tmp, rho_tmp)
    rho_aer[model] = rho_aer_tmp

plt.plot([],[],'k', label="$\tau_a(550) = 0.1$")
plt.plot([],[],'k-.', label="$\tau_a(550) = 0.2$")
for model in rho_aer.keys():
    plt.plot(wl, rho_aer[model], label=modelos[model])

rho_aer = {}
for model in modelos.keys():
    rho_aer_tmp = np.array([])
    for wa in tqdm(wl):
        s = pyOSOAA.OSOAA(logfile="/tmp/osoaa_ufm.log")
        # We configure a black ocean
        s = pyOSOAA.osoaahelpers.ConfigureOcean(s, ocean_type="black")
        # Ocean surface
        s.sea.wind = 0
        # Maritime Shettle and Fenn model
        s.aer.SetModel(model=model, sfmodel=3, rh=90)
        s.aer.aotref = 0.2
        # Relative azymuth angle
        s.view.phi = phi
        # Sun geometry
        s.ang.thetas = sun
        # We set the ap to zero
        s.view.level = 1
        s.ap.SetMot(0)

        # We run simulation
        s.wa = wa/1e3
        s.run()
        rho_tmp = np.interp(view, s.outputs.vsvza.vza, s.outputs.vsvza.I)/np.cos(sun*np.pi/180)
        rho_aer_tmp = np.append(rho_aer_tmp, rho_tmp)
    rho_aer[model] = rho_aer_tmp

plt.gca().set_prop_cycle(None)
for model in rho_aer.keys():
    plt.plot(wl, rho_aer[model],"-.")

#ax2 = ax1.twinx() 
#ax2.plot(wl, T, "k", alpha=0.5)
plt.xlabel(r"Longitud de onda [\si{\nano\meter}]")
plt.ylabel(r"$\rho$")
plt.legend()
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-aerosol.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-aerosol.png", dpi=300,bbox_inches='tight')
plt.close()