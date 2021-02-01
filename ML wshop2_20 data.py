import matplotlib.pyplot as plt
import numpy as np
#from keras.models import Sequential
#from keras.layers import Dense


X1 = np.random.randint(low=1, high=10, size=(20,))
X2 = np.random.randint(low=11, high=20, size=(20,))
X3 = np.random.randint(low=21, high=30, size=(20,))

Xa=[X1, X2];

Y1=[np.zeros(10), np.ones(10)];

X = np.linspace(0,20,20)

fig, ax = plt.subplots()
ax.plot(X,X1,'o')
ax.plot(X,X2,'x')
ax.plot(X,X3,'o')
plt.show()
