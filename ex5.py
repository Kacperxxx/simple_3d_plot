import numpy as np
import matplotlib.pyplot as plt


f = open("PCAdata.txt", 'r')

f.readline()
petal_length = list(map(float, f.readline().split()))
sepal_length = list(map(float, f.readline().split()))
sepal_width = list(map(float, f.readline().split()))

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.grid(b=True, color='grey', linestyle='-.', linewidth=0.3, alpha=0.2)

ax.scatter(petal_length, sepal_length, sepal_width, s=15, color='blue')
ax.set_xlim(5, 13)
ax.set_ylim(7, 16)
ax.set_zlim(4, 11)

petal_length_mean = np.mean(petal_length)
sepal_length_mean = np.mean(sepal_length)
sepal_width_mean = np.mean(sepal_width)
print(petal_length_mean, sepal_length_mean, sepal_width_mean)

x = np.array([petal_length, sepal_length, sepal_width])
x_covariance_matrix = np.cov(x, bias=True)


print(x_covariance_matrix)
print()
print(np.corrcoef(x))

plt.show()