import pandas as pd
import numpy as np

input_file = 'normalization_data.xls'
nd_data = pd.read_excel(input_file, header=None)

#最小最大规范化
print( (nd_data - nd_data.min()) / (nd_data.max() - nd_data.min()) )
#零均值规范化
print( (nd_data-nd_data.mean()) / nd_data.std() )
#小数定标规范化
k = np.ceil(np.log10(nd_data.abs().max()))
print(nd_data/10**k)

