import pandas as pd
import numpy as np
dict_data = {
	'student':['lilei','hanmeimei','madongmei'],
	'score':[98,99,100],
	'gender':['M','F','F']
}
data = pd.DataFrame(dict_data)
print(data)

data = pd.DataFrame(dict_data,columns=['gender','student','score'])
print(data)
print(data.columns)

#pandas数据的行列读取
data = pd.DataFrame(dict_data,
	columns = ['gender','student','score'],
	index = ['a','b','c'])
print(data)
print(data['student'])
print(data.student)
print(data.iloc[0])
print(data.loc['a'])
#修改一列的数据
data['score']=95
print(data)
data['score'] = range(95,98)
print(data)

score  = pd.Series([100,90,80],
	index = ['c','b','a'])
data['score'] = score
print(data)

# del data['score']
# print(data)

data = data.reindex(['c','b','a'])
print(data)

print('##############ffill################')
data = data.reindex(['c','a','b','d'],method='ffill')
print(data)

data = data.reindex(['c','a','b','d','e'],fill_value=0)
print(data)

print(data.dropna())