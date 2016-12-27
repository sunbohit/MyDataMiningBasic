import pandas as pd
 
#http://scikit-learn.org/stable/modules/feature_selection.html#randomized-sparse-models
from sklearn.linear_model import RandomizedLogisticRegression

#http://scikit-learn.org/stable/modules/linear_model.html#logistic-regression

input_file = 'bankloan.xls'

b_data = pd.read_excel(input_file)
#print(b_data.columns)
'''
Index(['年龄', '教育', '工龄', '地址', '收入', '负债率', '信用卡负债', '其他负债', '违约'], dtype='object')

'''
features = b_data.iloc[:,:8]
#print(type(features)) #<class 'pandas.core.frame.DataFrame'>
features = features.as_matrix()
#print(type(features)) #<class 'numpy.ndarray'>
labels = b_data.iloc[:,8].as_matrix()

randomized_logistic = RandomizedLogisticRegression()
randomized_logistic.fit(features,labels)
print(randomized_logistic.scores_)
'''
[ 0.105  0.085  1.     0.425  0.     1.     0.545  0.03 ]
'''
print(randomized_logistic.get_support())
'''
[False False  True  True False  True  True False]
'''
print('(稳定性选择)有效特征：%s'%','.join(b_data.columns[randomized_logistic.get_support()]))
'''
(稳定性选择)有效特征：工龄,地址,负债率,信用卡负债
'''
