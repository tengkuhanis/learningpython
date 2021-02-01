import matplotlib.pyplot as plt
import numpy as np
#from keras.models import Sequential
#from keras.layers import Dense


X1 = np.random.randint(low=1, high=10, size=(100,))
X2 = np.random.randint(low=11, high=20, size=(100,))
X3 = np.random.randint(low=21, high=30, size=(100,))

Xa=[X1, X2];

Y1=[np.zeros(10), np.ones(10)];

X = np.linspace(0,100,100)

fig, ax = plt.subplots()
ax.plot(X,X1,'o')
ax.plot(X,X2,'x')
ax.plot(X,X3,'o')
plt.show()