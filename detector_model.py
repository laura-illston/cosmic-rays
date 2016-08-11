## Calculates and plots detector model.

import math
import numpy as np
import matplotlib.pyplot as plt
import allen_model as am

## Plotting detection model (P(detection)|signal), signal = E_field_vals
  
E_field_vals = np.linspace(0.0,40.0,1000) 
P_detect_sig = np.empty(E_field_vals.size)
for i in range(0,E_field_vals.size):
  P_detect_sig[i] = am.prob_detection_signal(E_field_vals[i])

plt.clf()
plt.plot(E_field_vals, P_detect_sig, linewidth=2)
plt.title('Probability of Detecting Electric Field',fontsize=18)
plt.xlabel('$E_{max}$ ($\mu$V/m)',fontsize=18)
plt.ylabel('P(detection|field)',fontsize=18)
plt.ylim([0,1.1])
plt.grid()
plt.savefig('../figures/P_dect_field.pdf')
plt.show()