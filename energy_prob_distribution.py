## Using flux model to create an energy probability distribution

import math
import numpy as np
import matplotlib.pyplot as plt
import allen_model as am
 
obs_period = am.obs_period #Observation period (in s) that detector is running, needed
		           #to compute probability of detecting cosmic ray
obs_area = am.obs_area #Area over which we expect to be able to detect cosmic rays (m^2)

energy = 10**19
print('Number expected')
num = np.round(am.expected_num_particles(energy,obs_period,obs_area))
print(num)

