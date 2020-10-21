import numpy as np
data = np.genfromtxt('data.txt',delimiter=',')
print(data)
print(data.astype(int))