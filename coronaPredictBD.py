from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

### Load Data ###
data = pd.read_csv("cases.csv",sep=',')
data = data[['id','cases']]
print('-'*30);print(' Head ');print('-'*30)
print(data.head())

### prepare data ###
print('-'*30);print(' prepare data ');print('-'*30)
x = np.array(data['id']).reshape(-1,1)
y = np.array(data['cases']).reshape(-1,1)
plt.plot(y,'-m')
#plt.show()

polyFeatures = PolynomialFeatures(degree=17)
x = polyFeatures.fit_transform(x)
#print(x)

### Training Data ###
print('-'*30);print(' Training Data ');print('-'*30)
model = linear_model.LinearRegression()
model.fit(x,y)
accuracy = model.score(x,y)
print(f'Accuracy: {round(accuracy*100,3)}%')
y0 = model.predict(x)
plt.plot(y0,'--b')
#plt.show()

### Prediction ###
days = 2
print('-'*30);print(' Prediction ');print('-'*30)
print(f'Prediction-Cases after {days} Days: ',end='')
print(round(int(model.predict(polyFeatures.fit_transform([[245+days]])))/100000,5),'Lakhs')

x1 = np.array(list(range(1,245+days))).reshape(-1,1)
y1 = model.predict(polyFeatures.fit_transform(x1))
plt.plot(y1,'--r')
plt.plot(y0,'--b')
plt.show()
print(type(data))