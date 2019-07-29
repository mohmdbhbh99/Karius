import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38]).reshape((-1, 1))

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
# coefficient of determination (R^2)

print('intercept b0 =', model.intercept_)
# y_cut_part b0 = 5.633333333333329

print('slope b1 =', model.coef_)
# slope b1 = 0.54



x_new = np.array([5,10,40,15,20,50]).reshape((-1, 1))
y_new_predict = model.predict(x_new)
print('predicted values are :', y_new_predict)
# To Predict Response

summation = 0
n = len(x_new)
for i in range (0,n):
  difference = x_new[i] - y_new_predict[i]
  squared_difference = difference**2
  summation = summation + squared_difference
MSE = summation/n
print("MSE = ", MSE)

