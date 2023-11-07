from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = genfromtxt('insuranceBMI.csv', delimiter = ',', skip_header = 1)
split = np.hsplit(data, np.array([1,]))
arrX = split[0]
arrX = arrX.reshape(1338)
arrY = split[1]
arrY = arrY.reshape(1338)
xfit = np.linspace(0,70)
model = LinearRegression(fit_intercept = True)
model.fit(arrX[:, np.newaxis], arrY)

yfit = model.predict(xfit[:, np.newaxis])
plt.plot(xfit, yfit, color = "black")
plt.plot(arrX, arrY, 'o')

BMI =50
print("Parameters:", model.coef_, model.intercept_)
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("BMI:", BMI)
print("predict insurance charges :", model.predict([[BMI]]))

plt.show()