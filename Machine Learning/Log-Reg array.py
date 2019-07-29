import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

x1 = np.array([0,0.6,1.1,1.5,1.8,2.5,3,3.1,3.9,4,4.9,5,5.1])
y1 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
x2 = np.array([3,3.8,4.4,5.2,5.5,6.5,6,6.1,6.9,7,7.9,8,8.1])
y2 = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1])

X = np.array([0,0.6,1.1,1.5,1.8,2.5,3,3.1,3.9,4,4.9,5,5.1,3,3.8,4.4,5.2,5.5,6.5,6,6.1,6.9,7,7.9,8,8.1]).reshape((-1,1))
Y = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])

plt.plot(x1,y1,'ro',color='red')
plt.plot(x2,y2,'ro',color='blue')


model = LogisticRegression().fit(X,Y)


def logistic(classifier,X):
    return 1/(1+np.exp(-(model.intercept_ + model.coef_ * X)))

for i in range(1,120):
    plt.plot((i/10)-2,logistic(model,i/10),'ro',color='green')
plt.axis([-2,10,-0.5,2]) # area of box which we plot in (x1,x2,y1,y2)
plt.show()


print(model.predict(np.array([6]).reshape(-1,1)))
print(model.predict_proba(np.array([6]).reshape(-1,1)))



