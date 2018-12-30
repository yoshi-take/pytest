
import numpy as np
import matplotlib.pyplot as plt

img=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
plt.imshow(img,"gray")
plt.colorbar()
plt.show()