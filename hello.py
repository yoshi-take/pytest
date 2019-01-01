import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.where(x<=0,0,1)

def tanh_function(x):
    return np.tanh(x)

def relu_function(x):
    return np.where(x<=0,0,x)

def softmax_function(x):
    return np.exp(x)/np.sum(np.exp(x))

x=np.linspace(-5,5)
#y=relu_function(x)
y=softmax_function(np.array([1,2,3]))
print(y)

#plt.plot(x,y)
#plt.show()
