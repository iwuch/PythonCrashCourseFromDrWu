import pandas as pd
data = pd.DataFrame({
	'tag_id':['a','b','c','a','a','c'],
	'count':[10,30,20,10,15,22]
	})

grouped_data = data.groupby('tag_id')
print(grouped_data.sum())

book_name = pd.DataFrame({
		'book_name':['a','b','c','d','e','f'],
		'book_id':[11,22,33,44,55,66]
	})
id_rating = pd.DataFrame({
		'book_id':[11,22,22,44,55,66,33,11,55],
		'rating':[1,3,5,2,4,3,2,4,5]
	})
print(book_name)
print(id_rating)
print(pd.merge(book_name,id_rating))

data1 = pd.DataFrame({
		'key':['a','b','a','c','b','d'],
		'data1':[1,2,3,4,5,6]
	})

data2 = pd.DataFrame({
		'key':['a','b','c'],
		'data2':[8,9,7]
	})
print('*'*10)
print(pd.merge(data1,data2))
print('inner')
print(pd.merge(data1,data2,how='inner'))
print('outer')
print(pd.merge(data1,data2,how='outer'))
print('left')
print(pd.merge(data1,data2,how='left'))
print('right')
print(pd.merge(data1,data2,how='right'))
print('on=key')
print(pd.merge(data1,data2,on='key'))
print('*'*10)

data1 = pd.DataFrame({
		'key':['a','b','a','c','b','d'],
		'data':[1,2,3,4,5,6],
		'value1':[1,1,1,1,1,1],
	})

data2 = pd.DataFrame({
		'key':['a','b','c'],
		'data':[1,9,7],
		'value2':[2,2,2],
	})

print('data1,data2')
print(pd.merge(data1,data2,how='outer'))



data1 = pd.DataFrame({
		'lkey':['a','b','a','c','b','d'],
		'data':[1,2,3,4,5,6],
		'value1':[1,1,1,1,1,1],
	})

data2 = pd.DataFrame({
		'rkey':['a','b','c'],
		'data':[1,9,7],
		'value2':[2,2,2],
	})

print(pd.merge(data1,data2,
	left_on='lkey',right_on='rkey'))

#通过key来决定是否为一条记录，然后进行链接，统一个记录只占用一行