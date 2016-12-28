import pandas as pd
from sklearn.tree import DecisionTreeClassifier

input_file = 'sales_data.xls'
sd_data = pd.read_excel(input_file, index_col='序号')
#print(sd_data)
'''
   天气 是否周末 是否有促销 销量
序号                 
1   坏    是     是  高
2   坏    是     是  高
3   坏    是     是  高
4   坏    否     是  高
...
31  坏    是     否  低
32  好    否     是  低
33  好    否     否  低
34  好    否     否  低

'''
#print(sd_data == '好')
'''
天气   是否周末  是否有促销     销量
序号                            
1   False  False  False  False
2   False  False  False  False
3   False  False  False  False
4   False  False  False  False
...
31  False  False  False  False
32   True  False  False  False
33   True  False  False  False
34   True  False  False  False
'''
sd_data[sd_data == '好'] = 1 
sd_data[sd_data == '是'] = 1
sd_data[sd_data == '高'] = 1
sd_data[sd_data != 1 ] = -1
#print(sd_data)
'''
    天气 是否周末 是否有促销  销量
序号                   
1   -1    1     1   1
2   -1    1     1   1
3   -1    1     1   1
4   -1   -1     1   1
...
31  -1    1    -1  -1
32   1   -1     1  -1
33   1   -1    -1  -1
34   1   -1    -1  -1
'''

feature = sd_data.iloc[:,:3].as_matrix()
label = sd_data.iloc[:,3].as_matrix()
#print(type(feature)) #<class 'numpy.ndarray'>
#print(type(label)) #<class 'numpy.ndarray'>

dtc = DecisionTreeClassifier(criterion='entropy')
dtc.fit(feature,label)

