import pandas as pd
data = pd.read_csv('books/dbrating.csv')
print(data)

data = pd.read_csv('books/dbrating.csv',header=None)
print(data)

data = pd.read_csv('books/dbrating.csv',
	names=['user_id','book_id','rating'],
	sep=',')

print(data)

