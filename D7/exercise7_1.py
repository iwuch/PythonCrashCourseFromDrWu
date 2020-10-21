import numpy as np
data = np.genfromtxt('books/rating.txt',delimiter=',')
data = data.astype(int)
rating_sum = np.zeros(10000)
rating_people_count = np.zeros(10000)
for rating in data:
	book_id = rating[1] - 1
	rating_sum[book_id] += rating[2]
	rating_people_count[book_id] += 1
print(rating_sum)
print(rating_people_count)
print(rating_sum/rating_people_count)