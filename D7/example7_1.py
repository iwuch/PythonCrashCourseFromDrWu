import numpy as np
import time
list_array = list(range(int(1e6)))
start_time = time.time()
python_array = [val*5 for val in list_array]
end_time = time.time()
print(f'Python array time:{1000*(end_time-start_time)}ms')

np_array = np.arange(1e6)
start_time = time.time()
np_array = np_array*5
end_time = time.time()
print(f'Numpy array time:{1000*(end_time-start_time)}ms')