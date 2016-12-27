import pandas as pd

input_file = 'bankloan.xls'

b_data = pd.read_excel(input_file)
features = b_data.iloc[:,:8]
#print(type(features)) #<class 'pandas.core.frame.DataFrame'>
features = features.as_matrix()
#print(type(features)) #<class 'numpy.ndarray'>
labels = b_data.iloc[:,8].as_matrix()


