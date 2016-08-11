## Using prob_particle from allen_model.py to plot probability of detection versus E_p for given 
## (x,y), zenith angle and geomagnetic angle, assuming that such a shower has occured.

import math
import numpy as np
import matplotlib.pyplot as plt
import allen_model as am

R_0 = 100 #frequency and zenith angle dependent parameter in Allen formula (m)

x1 = 100 #m
y1 = 100 #m
zenith1 = 30 #zenith angle of air-shower axis in degrees
geo_angle1 = 30 #degrees

zenith_max = 0 #zenith angle that produces maximum value of signal (degrees)
geo_angle_max = 90 #geomagnetic angle that produces maximum value of signal (degrees)
x_max = 0 #x co-ordinate to produce maximum signal (m)
y_max = 0 #y co-ordinate to produce maximum signal (m)

def plot_detection_given_shower(x_pos,y_pos,zenith,geo_angle,ax):
  E_p_vals = np.logspace(14.0, 20.0, num=10000)
  prob_particle_vals = np.empty(E_p_vals.size)
  for i in range(0,E_p_vals.size):
    prob_particle_vals[i] = am.prob_detection_field(x_pos,y_pos,R_0,zenith,geo_angle,E_p_vals[i])

  ax.plot(E_p_vals,prob_particle_vals, linewidth=2)
  ax.set_xscale('log')
  ax.set_ylim([0,1.1])
  textstr = '$R =%.2f$ m \n $\\theta =%.2f \degree$ \n $\\alpha =%.2f \degree$'%(math.sqrt(x_pos**2 + y_pos**2), zenith,geo_angle)
  ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
	verticalalignment='top', bbox=dict(facecolor='white', edgecolor='black',pad=5.0))
  ax.grid()
  
######################################################################################################################################

#### Creating plots to show the effect of energy on the probability of detection

###fig = plt.figure()
###ax = fig.add_subplot(111)

###plot_detection_given_shower(0,0,0,90,ax)
###ax.set_title('Probability of Detecting Cosmic Rays of Energy E$_p$ \n',fontsize=18)
###ax.set_xlabel('Energy (E$_p$) (eV)',fontsize=18)
###ax.set_ylabel('P(detection | signal)' ,fontsize=18)

###plt.savefig('../figures/detect_sig_energy.pdf')
###plt.show()

#########################################################################################################################################

#### Creating plots to show the effect of lateral distance on the probability of detection

###fig = plt.figure()
###ax = fig.add_subplot(111)    # The big subplot
###ax.set_title('Effect of Lateral Distance on Probability of Detection \n',fontsize=18)
###ax.set_xlabel('Energy (E$_p$) (eV)',fontsize=18)
###ax.set_ylabel('P(detection | signal)' ,fontsize=18)
###fig.patch.set_facecolor('white')
#### Turn off axis lines and ticks of the big subplot
###ax.spines['top'].set_color('none')
###ax.spines['bottom'].set_color('none')
###ax.spines['left'].set_color('none')
###ax.spines['right'].set_color('none')
###ax.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')

###ax1 = fig.add_subplot(221)
###plot_detection_given_shower(0,0,zenith_max,geo_angle_max,ax1)

###ax2 = fig.add_subplot(222)
###plot_detection_given_shower(100,100,zenith_max,geo_angle_max,ax2)

###ax3 = fig.add_subplot(223)
###plot_detection_given_shower(300,300,zenith_max,geo_angle_max,ax3)

###ax4 = fig.add_subplot(224)
###plot_detection_given_shower(700,700,zenith_max,geo_angle_max,ax4)

####plt.savefig('../figures/detect_sig_lateral.pdf')
###plt.show()

#########################################################################################################################################

####Creating plots to show the effect of zenith angle on the probability of detection

###fig = plt.figure()
###ax = fig.add_subplot(111)    # The big subplot
###ax.set_title('Effect of Zenith Angle on Probability of Detection \n',fontsize=18)
###ax.set_xlabel('Energy (E$_p$) (eV)',fontsize=18)
###ax.set_ylabel('P(detection | signal)' ,fontsize=18)
###fig.patch.set_facecolor('white')
####Turn off axis lines and ticks of the big subplot
###ax.spines['top'].set_color('none')
###ax.spines['bottom'].set_color('none')
###ax.spines['left'].set_color('none')
###ax.spines['right'].set_color('none')
###ax.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')

###ax1 = fig.add_subplot(221)
###plot_detection_given_shower(x1,y1,0,geo_angle1,ax1)

###ax2 = fig.add_subplot(222)
###plot_detection_given_shower(x1,y1,30,geo_angle1,ax2)

###ax3 = fig.add_subplot(223)
###plot_detection_given_shower(x1,y1,70,geo_angle1,ax3)

###ax4 = fig.add_subplot(224)
###plot_detection_given_shower(x1,y1,90,geo_angle1,ax4)

###plt.savefig('../figures/detect_sig_zenith.pdf')
###plt.show()

#########################################################################################################################################

### Creating plots to show the effect of geomagnetic angle on the probability of detection

fig = plt.figure()
ax = fig.add_subplot(111)    # The big subplot
ax.set_title('Effect of Geomagnetic Angle on Probability of Detection \n',fontsize=18)
ax.set_xlabel('Energy (E$_p$) (eV)',fontsize=18)
ax.set_ylabel('P(detection | signal)' ,fontsize=18)
fig.patch.set_facecolor('white')
# Turn off axis lines and ticks of the big subplot
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')

ax1 = fig.add_subplot(221)
plot_detection_given_shower(x1,y1,zenith1,0,ax1)

ax2 = fig.add_subplot(222)
plot_detection_given_shower(x1,y1,zenith1,90,ax2)

ax3 = fig.add_subplot(223)
plot_detection_given_shower(x1,y1,zenith1,179,ax3)

ax4 = fig.add_subplot(224)
plot_detection_given_shower(x1,y1,zenith1,180,ax4)

plt.savefig('../figures/detect_sig_geo.pdf')
plt.show()