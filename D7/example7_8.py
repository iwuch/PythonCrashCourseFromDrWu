import pandas as pd
import numpy as np
dict_data = {
	"Beijing":1000,
	"Shanghai":800,
	"Shenzhen":500
}

data = pd.Series(dict_data)
print(data)

index_list = ['Guangzhou','Shanghai','Beijing','Shenzhen']
data = pd.Series(dict_data,index = index_list)
print(data)
print(data.isnull())
print(data*2)
print(np.square(data))

print(data)
data.name = 'CityData'
data.index.name = 'City'
print(data)