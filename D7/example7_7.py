import pandas as pd
list_data = [1,3,5,7]
data = pd.Series(list_data)
print(data)
print(data.values)
print(data.index)

data = pd.Series(list_data,index=['a','j','k','z'])
print(data)
data.index = ['z','x','c','a']
print(data)
print(len(data))
print(data['a'])
print(data[['a','x','c']])
print(data[0:2])
print(data.value_counts())
print('a' in data)
print('b' in data)
