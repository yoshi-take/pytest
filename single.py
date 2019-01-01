import numpy as np
import matplotlib.pyplot as plt

#x,y座標
X=np.arange(-1.0,1.0,0.2)
Y=np.arange(-1.0,1.0,0.2)

#出力層を格納
Z=np.zeros((10,10))

#x,y座標の重み
w_x=2.5
w_y=3.0

#バイアス
bias=0.1

#グリッドの各マスでニューロンの演算
for i in range(10):
    for j in range(10):

        #入力の重みの積の総和+バイアス
        u = X[i]*w_x + Y[j]*w_y + bias

        #グリッドに出力を格納
        y=1/(1+np.exp(-u))  #sigmoid
        Z[j][i]=y


#グリッドの表示
plt.imshow(Z,"gray",vmin=0.0,vmax=1.0)
plt.colorbar()
plt.show()

