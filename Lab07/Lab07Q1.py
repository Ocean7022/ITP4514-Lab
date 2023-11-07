import numpy as np
import matplotlib.pyplot as plt
import sklearn   # This imports the scikit-learn library
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

rng = np.random.RandomState(1)
arrX = 10 * rng.rand(50)
arrY = 3 * arrX - 5 + rng.randn(50)
model=LinearRegression(fit_intercept=True)
model.fit(arrX[:,np.newaxis], arrY)
xfit=np.linspace(0,10)
yfit=model.predict(xfit[:, np.newaxis])
plt.plot(xfit,yfit, color="black")
plt.plot(arrX,arrY, 'o')
# The following will draw as many line segments as there are columns in matrices x and y
plt.plot(np.vstack([arrX,arrX]), np.vstack([arrY, model.predict(arrX[:, np.newaxis])]), color="red")

print("Parameters:", model.coef_, model.intercept_)
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

plt.show()

print("Mean Squared Error:",mean_squared_error([arrY[10]], model.predict([[arrX[10]]])))