import pandas as pd
 
#http://scikit-learn.org/stable/modules/feature_selection.html#randomized-sparse-models
from sklearn.linear_model import RandomizedLogisticRegression

#http://scikit-learn.org/stable/modules/feature_selection.html#rfe
from sklearn.feature_selection import RFE
from sklearn.svm import SVR

#http://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
from sklearn.linear_model import LogisticRegression as LogisticRegression

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
print('(稳定性选择)有效特征：%s'%','.join(b_data.columns[:-1][randomized_logistic.get_support()]))
'''
(稳定性选择)有效特征：工龄,地址,负债率,信用卡负债
'''
feat_1 = b_data[b_data.columns[:-1][randomized_logistic.get_support()]].as_matrix()

estimator = SVR(kernel="linear")
RFE_selector = RFE(estimator=estimator, n_features_to_select=None, step=1)
RFE_selector.fit(features,labels)
print(RFE_selector.support_)
'''
[False  True  True False False  True  True False]
'''
print(RFE_selector.ranking_)
'''
[5 1 1 3 4 1 1 2]
'''
print('(递归特征消除)有效特征：%s'%','.join(b_data.columns[:-1][RFE_selector.get_support()]))

'''
(递归特征消除)有效特征：教育,工龄,负债率,信用卡负债
'''
feat_2 = b_data[b_data.columns[:-1][RFE_selector.get_support()]].as_matrix()

lr_1 = LogisticRegression()
lr_1.fit(feat_1,labels)
print('(稳定性选择)平均正确率为：%s' % lr_1.score(feat_1,labels))
'''
(稳定性选择)平均正确率为：0.814285714286
'''

lr_2 = LogisticRegression()
lr_2.fit(feat_1,labels)
print('(递归特征消除)平均正确率为：%s' % lr_2.score(feat_2,labels))
'''
(递归特征消除)平均正确率为：0.717142857143

'''
