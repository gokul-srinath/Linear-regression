import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('ex1data1.txt',header=None)
data.columns=['Population(10,000s)','Profit($10,000)']

X=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
np.isnan(X).any()
pd.isnull(y).any()

plt.scatter(X,y,color='red',marker='+')
plt.xlabel('Population')
plt.ylabel('profit')
plt.title('Population vs profit')

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)

plt.plot(X,regressor.predict(X),color='blue')
s=regressor.predict(X)
from sklearn.metrics import mean_squared_error as mse
mse1=mse(regressor.predict(X),y)/2