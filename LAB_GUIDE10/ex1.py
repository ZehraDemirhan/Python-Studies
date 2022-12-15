import matplotlib.pyplot as plt
import numpy as np

plt.clf()#clear the screen 
x = np.arange(1,11)
y = x**2
plt.plot(x,y,'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y is equal to x squared')
plt.legend(['y = x**2'])

plt.show()
