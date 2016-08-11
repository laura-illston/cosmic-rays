## Combines flux model and probability models and uses a brute-force integration
## technique to model the absolute probability of detecting a high-energy cosmic
## ray over a given time frame.

import math
import numpy as np
import matplotlib.pyplot as plt
import allen_model as am

R_0 = 100 #frequency and zenith angle dependent parameter in Allen formula (m)

#### Need to integrate prob_detection_field (from allen_model.py) over x,y,zenith,geo_angle for a given E_p
#### Don't need to know flux for this step - assumption is that an air-shower has occured.
#### We start by using a brute force method, keeping track of the number of times that the produced
#### electric field is detected.

### Repeating for a range of energies and then plotting the results

##E_p_vals = np.logspace(11.0, 20.0, num=20)
##prob_array = np.empty(E_p_vals.size)

##for i in range(0,E_p_vals.size):
  ##num_showers = 0.0
  ##prob_sum = 0.0 #Sum of the probabitities of detecting each shower
  ##for x in np.linspace(-1000,1000,10):
    ##for y in np.linspace(-1000,1000,10):
      ##for theta in np.linspace(0,np.pi/2,10):
	##for alpha in np.linspace(-np.pi,np.pi,10):
	  ##prob_sum = prob_sum + am.prob_detection_field(x,y,R_0,theta,alpha,E_p_vals[i])
	  ##num_showers = num_showers + 1
  ##prob_array[i] = prob_sum/num_showers 
  
###print 'num_showers = ' + str(num_showers) + '\n'
###print 'prob_sum = ' + str(prob_sum) + '\n'
###print 'prob_sum/num_showers = ' + str(prob_sum/num_showers) + '\n'

##plt.plot(E_p_vals, prob_array, linewidth=2)
##plt.xscale('log')
##plt.title('Probabilities of Detecting Cosmic Rays, \n Given that an Air Shower has Occured',fontsize=18)
##plt.xlabel('Energy (E$_p$) (eV)',fontsize=18)
##plt.ylabel('P(detection | all signals)',fontsize=18)
##plt.grid()
###plt.savefig('../figures/P_dect_field_mult.pdf')
##plt.show()

##########################################################################################################

## Repeating brute-force integrating for specific energy values

new_E_p_array = np.array([10**16, 10**17, 10**18, 10**19, 10**20])
prob_array2 = np.empty(new_E_p_array.size)

for i in range(0,new_E_p_array.size):
  num_showers = 0.0
  prob_sum = 0.0 #Sum of the probabitities of detecting each shower
  for x in np.linspace(-1000,1000,10):
    for y in np.linspace(-1000,1000,10):
      for theta in np.linspace(0,np.pi/2,10):
	for alpha in np.linspace(-np.pi,np.pi,10):
	  prob_sum = prob_sum + am.prob_detection_field(x,y,R_0,theta,alpha,new_E_p_array[i])
	  num_showers = num_showers + 1
  prob_array2[i] = prob_sum/num_showers 
  
num = 1  
print(prob_array2)
print(1 - prob_array2)
print(1- ((1 - prob_array2)**num))

