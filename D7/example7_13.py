import pandas as pd
import numpy as np
import time

start_time = time.time()
data = np.genfromtxt('books/dbrating.csv',delimiter=',')
end_time = time.time()
print(f'Numpy reading time:{1000*(end_time-start_time)}ms')

start_time = time.time()
data = pd.read_csv('books/dbrating.csv',header=None)
end_time = time.time()
print(f'Pandas reading time:{1000*(end_time-start_time)}ms')