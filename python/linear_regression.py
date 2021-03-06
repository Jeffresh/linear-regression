import numpy as np
import scipy as sc
import matplotlib.pyplot as plt


from sklearn.datasets import load_boston
boston = load_boston()

X = np.array(boston.data[:, 5])
Y = np.array(boston.target)

plt.scatter(X,Y, alpha=0.3)


X = np.array([np.ones(506), X]).T

B = np.linalg.inv(X.T @ X) @ X.T @ Y


plt.plot([4,9],[B[0] + B[1] *4, B[0] + B[1] * 9],c='red')
plt.show()