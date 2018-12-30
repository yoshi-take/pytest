import numpy as np
import matplotlib.pyplot as plt

x=np.random.normal(50,10,10000)

print(np.average(x))
print(np.std(x))

plt.hist(x,bins=50)
plt.show()