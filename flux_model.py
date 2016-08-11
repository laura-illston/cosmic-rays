## Calculates and plots modelled cosmic ray flux versus energy.

import math
import numpy as np
import matplotlib.pyplot as plt
import allen_model as am

## Plotting 'flux versus energy' model
E_p_vals = np.logspace(8.0, 20.0, num=10000)
flux_vals = np.empty(E_p_vals.size)
for i in range(0,flux_vals.size):
  flux_vals[i] = am.flux_primary(E_p_vals[i])
  
plt.clf()
plt.plot(E_p_vals,flux_vals, linewidth=2)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Energy (eV)',fontsize=18)
plt.ylabel('Flux (m$^2$ sr s GeV)$^{-1}$',fontsize=18)
plt.title('Cosmic Ray Flux',fontsize=18)
plt.ylim([10**-31,10**5])
plt.grid()
plt.savefig('../figures/unscaled_flux_energy.pdf')
plt.show()

## Plotting 'scaled flux versus energy' model (multiplying flux by E**2.6,
## where E is the energy of the cosmic ray).

E_p_vals2 = np.logspace(13.0, 20.0, num=10000)
flux_vals2 = np.empty(E_p_vals2.size)
for i in range(0,flux_vals2.size):
  flux_vals2[i] = am.flux_primary(E_p_vals2[i])

scaled_flux_vals = np.empty(flux_vals2.size)
for i in range(0,scaled_flux_vals.size):
  scaled_flux_vals[i] = flux_vals2[i]*(E_p_vals2[i]/10**9)**2.6

plt.clf()
plt.plot(E_p_vals2,scaled_flux_vals, linewidth=2)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Energy (E) (eV)',fontsize=18)
plt.ylabel('E$^{2.6}$*Flux (GeV$^{1.6}$ m$^{-2}$ s$^{-1}$ sr$^{-1}$)',fontsize=18)
plt.title('Scaled Cosmic Ray Flux',fontsize=18)
plt.grid()
plt.savefig('../figures/scaled_flux_energy.pdf')
plt.show()