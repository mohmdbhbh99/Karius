import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt



dataset = pd.read_csv("housing.csv")
size = dataset['size']
price = dataset['price']

x = np.array(size).reshape((-1, 1))
y = np.array(price).reshape((-1, 1))
model = LinearRegression().fit(x, y)

plt.scatter(x,y,color='green')
plt.plot(x,model.predict(x),color='red')
plt.xlabel('size')
plt.ylabel('price')
plt.show()