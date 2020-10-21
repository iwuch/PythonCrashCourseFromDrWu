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