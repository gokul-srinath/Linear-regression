import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('ex1data1.txt',header=None)
data.columns=['Population(10,000s)','Profit($10,000)']

X=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
y=np.reshape(y,(len(y),1))
np.isnan(X).any()
pd.isnull(y).any()

plt.scatter(X,y,color='red',marker='+')
plt.xlabel('Population')
plt.ylabel('profit')
plt.title('Population vs profit')


#cost function
ones=np.ones((np.shape(X)[0],1))

X=np.concatenate((ones,X),axis=1)
theta=np.zeros((np.shape(X)[1],1))

def cost(X,y,theta):
    h=np.subtract(np.matmul(X,theta),y)
    h=np.matmul(np.transpose(h),h)/(2*len(y))
    return h
J=cost(X,y,theta)
print(J)
#gradient descent
alpha=0.03
n=1500
t0=np.linspace(-10,10,100)
t1=np.linspace(-1,4,100)
J_vals=np.zeros((len(t0),len(t1)))
for i in range(len(t0)):
    for j in range(len(t1)):
        J_vals[i,j]=cost(X,y,[[t0[i]],[t1[j]]])
J_vals=np.transpose(J_vals)
from mpl_toolkits import mplot3d
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib','qt')
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(t0,t1,J_vals)
plt.show()
fig1=plt.figure()
plt.contour(t0,t1,J_vals,np.logspace(-3,2,20))

