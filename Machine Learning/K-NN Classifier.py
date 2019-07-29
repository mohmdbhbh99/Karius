import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

xBlue = np.array([0.3,0.5,1,1.4,1.7,2])
yBlue = np.array([1,4.5,2.3,1.9,8.9,4.1])
xRed = np.array([3.3,3.5,4,4.4,5.7,6])
yRed = np.array([7,1.5,6.3,1.9,2.9,7.1])

X = np.array([[0.3,1],[0.5,4.5],[1,2.3],[1.4,1.9],[1.7,8.9],[2,4.1],[3.3,7],[3.5,1.5],[4,6.3],[4.4,1.9],[5.7,2.9],[6,7.1]])
Y = np.array([0,0,0,0,0,0,1,1,1,1,1,1]) # 0 is blue class , 1 is red class

plt.plot(xRed,yRed,'ro',color='red')
plt.plot(xBlue,yBlue,'ro',color='blue')

plt.plot(3,5,'ro',color='yellow',markersize=8)
plt.axis([-0.5,10,-0.5,10])
k = 3
classifier = KNeighborsClassifier(n_neighbors=k).fit(X,Y)

pred = classifier.predict(np.array([[4,5]]))
print(pred)
plt.show()