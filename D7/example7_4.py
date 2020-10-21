import numpy as np
data = np.arange(10)
print(data)
#numpy数组的整形
print(data.reshape((2,5)))
print(data.reshape((2,5)).T)
#numpy数组的运算
print(np.sqrt(data))
data1 = np.array([1,3,5,7,9])
data2 = np.array([2,4,6,8,10])
print(data2+data1)
print(np.add(data1,data2))
#numpy的统计学方法
print(data.sum())
print(data.mean())
print(data.std())


