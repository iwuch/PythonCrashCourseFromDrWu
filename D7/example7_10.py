import pandas as pd
import numpy as np
dict_data = {
	'student':['lilei','hanmeimei','madongmei'],
	'score':[98,99,100],
	'gender':['M','F','F']
}
data = pd.DataFrame(dict_data,index =['a','b','c'])
print(data)
data = data.reindex(['c','b','a'])
print(data)
data = data.reindex(['c','a','b','d'],method='bfill')
print(data)

print(data[data['score']>=99])

selected_list = [99]
print(data[data['score'].isin(selected_list)])

print(data.sort_index())
print(data.sort_index(ascending=False))
print(data.sort_values(by='score'))
print(data.sum())
