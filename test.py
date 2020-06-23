import ctypes
_bilinear=ctypes.CDLL('./bilinear.so')
_bilinear.init_scatt_bilinear.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))
_bilinear.interp_scatt_bilinear.argtypes = (ctypes.c_double, ctypes.c_double)
_bilinear.interp_scatt_bilinear.restype = ctypes.c_double
def init_bilinear(f,x,y):
    global _bilinear
    input_array1 = (ctypes.c_double * 4)(*f)
    input_array2 = (ctypes.c_double * 4)(*x)
    input_array3 = (ctypes.c_double * 4)(*y)
    _bilinear.init_scatt_bilinear(input_array1, input_array2, input_array3) 
    return
def get_bilinear(x_tar,y_tar):
    global _bilinear
    val=_bilinear.interp_scatt_bilinear(ctypes.c_double(x_tar), ctypes.c_double(y_tar))
    return float(val)


#simple animation for testing

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
nx=256
ny=256

x = np.linspace(-100, 100, nx)
y = np.linspace(-100, 100, ny)
zz,zz = np.meshgrid(x, y, sparse=False)
f=[20.,-5.,50.,-10.]
xin=[50.,15.,-3.,90.]
yin=[-30.,10.,0.,25.]
fig=plt.figure()
def animate(i):
    u=i*2.*3.14/200.
    xin[3]=50.*np.sin(u)
    yin[3]=50.*np.cos(u)
    init_bilinear(f,xin,yin) #initialize interpolation
    for ii in range(nx):
        for j in range(ny):
            zz[ii,j]=get_bilinear(x[ii],y[j])
    plt.contourf(x,y,zz)
    cont=plt.scatter(xin,yin,s=20,c='black',marker='o')
    return cont
anim = FuncAnimation(fig, animate, interval=100, frames=200,repeat=False)
anim.save('anim.mp4')
plt.draw()
plt.show()
