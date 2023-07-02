#Here we will add some python code

import numpy as np
import matplotlib.pyplot as plt

#Create some data
xvec = np.linspace(0,1,100)
a,b,c = np.random.normal(size=3, )
yvec = a*xvec**2 + b*xvec + c
y = yvec + 0.15*np.random.normal(size=len(xvec))

#Plot the data
plt.figure()
plt.plot(xvec,y,'ro')

#Fit the data
#Let's use a 3rd degree polynomial this time.
p = np.polyfit(xvec,y,3)
fit_values = np.polyval(p,xvec)
plt.plot(xvec,fit_values, 'b--')
plt.legend(loc='best')
