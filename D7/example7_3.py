import numpy as np
#创建一个全是1的二维数组
data = np.ones((3,10))
print(data)
#获取数组中某个数字（索引）
data = np.arange(10)
print(data[5])
#获取数组中某几个数字（行话：切片）
#切片的拷贝
data_slice = data[3:6].copy()
data_slice[2] = 100
print(data)
#如果不适用拷贝将改变原来的值
data_slice = data[3:6]
data_slice[2] = 100
print(data)
#多维数组中元素的索引
data = np.array([[1,2,3],[4,5,6]])
print(data[0][1])
print(data[0,1])
