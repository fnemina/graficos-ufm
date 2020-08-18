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

wl = np.array([412., 443., 490., 510., 555., 670., 765., 865.])
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
chl = 1
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


t = np.exp(-tau_ray/2*(1+1/np.cos(view*np.pi/180)))
plt.plot(wl, rho_toa*T, "ok", label=r"$\rho_{toa}$ - medición del satélite")
plt.ylabel(r"$\rho$")
plt.legend()
plt.ylim(-0.005,0.175)
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction0.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction0.png", dpi=300,bbox_inches='tight')
plt.close()

plt.plot(wl, rho_toa*T, "ok", label=r"$t_g \rho_{toa}$ - medición del satélite", alpha=0.5)
plt.plot(wl, rho_toa, "ok", label=r"$\rho_{toa}$ - corregido por absorción de gases")
plt.ylabel(r"$\rho$")
plt.legend()
plt.ylim(-0.005,0.175)
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction1.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction1.png", dpi=300,bbox_inches='tight')
plt.close()

plt.plot(wl, rho_toa, "ok", label=r"$\rho_{toa}$ - corregido por absorción de gases", alpha=0.3)
plt.plot(wl, rho_toa-rho_ray, "oC0", label=r"$\rho_{toa} - \rho_{R}$ - corregido por Rayleigh")
plt.ylabel(r"$\rho$")
plt.legend()
plt.ylim(-0.005,0.175)
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction2.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction2.png", dpi=300,bbox_inches='tight')
plt.close()

plt.plot(wl, rho_toa, "ok", label=r"$\rho_{toa}$ - corregido por absorción de gases", alpha=0.3)
plt.plot(wl, rho_toa-rho_ray, "oC0", label=r"$\rho_{toa} - \rho_{R}$ - corregido por Rayleigh", alpha=0.3)
plt.plot(wl, rho_toa-rho_ray-rho_gli, "oC3", label=r"$\rho_{toa} - \rho_{R} - T\rho_{g} - t \rho_{wc}$ - corregido por glint y whitecaps")
plt.ylabel(r"$\rho$")
plt.legend()
plt.ylim(-0.005,0.175)
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction3.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction3.png", dpi=300,bbox_inches='tight')
plt.close()

plt.plot(wl, rho_toa-rho_ray-rho_gli, "oC3", label=r"$\rho_{toa} - \rho_{R} - T\rho_{g} - t \rho_{wc}$ - corregido por glint y whitecaps")
plt.plot(wl[-2:], wl[-2:]*0, "ok", label=r"$\rho_{toa} - \rho_{R} - T\rho_{g} - t \rho_{wc}$ - señal esperada debido al agua")
plt.annotate("", xy=(765, (rho_toa-rho_ray-rho_gli)[-2]), xytext=(765, 0),
             arrowprops=dict(arrowstyle="->"))
plt.annotate("", xy=(865, (rho_toa-rho_ray-rho_gli)[-1]), xytext=(865, 0),
             arrowprops=dict(arrowstyle="->"))
plt.text(x=815, y = 0.004, s=r"\large$\rho_a + \rho_{aR}$", horizontalalignment='center', verticalalignment='center')
#plt.plot()
plt.ylabel(r"$\rho$")
plt.legend()
plt.ylim(-0.005,0.025)
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction4.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction4.png", dpi=300,bbox_inches='tight')
plt.close()

plt.plot(wl, rho_toa-rho_ray-rho_gli, "oC3", label=r"$\rho_{toa} - \rho_{R} - T\rho_{g} - t \rho_{wc}$ - corregido por glint y whitecaps")
plt.plot(wl[-2:], wl[-2:]*0, "ok", label=r"$\rho_{toa} - \rho_{R} - T\rho_{g} - t \rho_{wc}$ - señal esperada debido al agua")
plt.plot(wl, rho_aer, "-C0", label=r"$\rho_{a} + \rho_{aR} $ - señal ajustada de aerosoles")
plt.annotate("", xy=(765, (rho_toa-rho_ray-rho_gli)[-2]), xytext=(765, 0),
             arrowprops=dict(arrowstyle="->"))
plt.annotate("", xy=(865, (rho_toa-rho_ray-rho_gli)[-1]), xytext=(865, 0),
             arrowprops=dict(arrowstyle="->"))
plt.text(x=815, y = 0.004, s=r"\large$\rho_a + \rho_{aR}$", horizontalalignment='center', verticalalignment='center')
#plt.plot()
plt.ylabel(r"$\rho$")
plt.legend()
plt.ylim(-0.005,0.025)
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction5.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction5.png", dpi=300,bbox_inches='tight')
plt.close()


plt.plot(wl, rho_toa, "ok", label=r"$\rho_{toa}$ - corregido por absorción de gases", alpha=0.3)
plt.plot(wl, rho_toa-rho_ray, "oC0", label=r"$\rho_{toa} - \rho_{R}$ - corregido por Rayleigh", alpha=0.3)
plt.plot(wl, rho_toa-rho_ray-rho_gli, "oC3", label=r"$\rho_{toa} - \rho_{R} - T\rho_{g} - t \rho_{wc}$ - corregido por glint y whitecaps", alpha=0.3)
plt.plot(wl, rho_toa-rho_ray-rho_gli-rho_aer, "sC0", label=r"$\rho_{toa} - \rho_{R} - T\rho_{g} - t \rho_{wc} - \rho_a - \rho_{aR}$ - corregido aerosoles")
plt.ylabel(r"$\rho$")
plt.legend()
plt.ylim(-0.005,0.175)
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction6.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction6.png", dpi=300,bbox_inches='tight')
plt.close()

plt.plot(wl, rho_toa, "ok", label=r"$\rho_{toa}$ - corregido por absorción de gases", alpha=0.3)
plt.plot(wl, rho_toa-rho_ray, "oC0", label=r"$\rho_{toa} - \rho_{R}$ - corregido por Rayleigh", alpha=0.3)
plt.plot(wl, rho_toa-rho_ray-rho_gli, "oC3", label=r"$\rho_{toa} - \rho_{R} - T\rho_{g} - t \rho_{wc}$ - corregido por glint y whitecaps", alpha=0.3)
plt.plot(wl, rho_toa-rho_ray-rho_gli-rho_aer, "sC0", label=r"$\rho_{toa} - \rho_{R} - T\rho_{g} - t \rho_{wc} - \rho_a - \rho_{aR}$ - corregido aerosoles", alpha=0.3)
plt.plot(wl, (rho_toa-rho_ray-rho_gli-rho_aer)/t, "oC2", label=r"$(\rho_{toa} - \rho_{R} - T\rho_{g} - t \rho_{wc} - \rho_a - \rho_{aR})$ - corregido por absorción no gaseosa")
plt.ylabel(r"$\rho$")
plt.legend()
plt.ylim(-0.005,0.175)
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction7.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction7.png", dpi=300,bbox_inches='tight')
plt.close()

plt.plot(wl, (rho_toa-rho_ray-rho_gli-rho_aer)/t, "oC2", label=r"$(\rho_{toa} - \rho_{R} - T\rho_{g} - t \rho_{wc} - \rho_a - \rho_{aR})/t$ - corregido por absorción no gaseosa")
plt.plot(wl, rho_chl, "C2",label=r"Señal esperada")
plt.ylabel(r"$[\rho]_N$")
plt.legend()
plt.ylim(-0.005,0.025)
plt.tight_layout()
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction8.pdf", bbox_inches='tight')
plt.savefig(f"curso-ico/figs/fig:t3-atmospheric_correction8.png", dpi=300,bbox_inches='tight')
plt.close()