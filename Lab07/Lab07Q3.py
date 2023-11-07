from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

data = genfromtxt('insuranceBMI.csv', delimiter=',', skip_header = 1)
X = np.array(data)

model = KMeans(3)
model.fit(X)
print(type(X))
print(model.cluster_centers_)

plt.scatter(X[:,0],X[:,1], c=model.labels_)
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], s=100, color="red")

plt.show()