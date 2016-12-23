import pandas as pd

datafile = 'discretization_data.xls'
dd_data = pd.read_excel(datafile)
#print(dd_data)
dd_data = dd_data['肝气郁结证型系数'].copy()
#print(dd_data)

k = 4

#等宽离散化
d_w = pd.cut(dd_data,k,labels=range(k))
#print(d_w)

#等频离散化
w = [1.0*i/k for i in range(k+1)]
#print(w) # [0.0, 0.25, 0.5, 0.75, 1.0]
#print(dd_data.describe(percentiles = w))
'''
count    930.000000
mean       0.232154
std        0.078292
min        0.026000
0%         0.026000
25%        0.176250
50%        0.231000
75%        0.281750
100%       0.504000
max        0.504000
Name: 肝气郁结证型系数, dtype: float64
'''
w = dd_data.describe(percentiles = w)[4:9]
#print(w)
'''
0%      0.02600
25%     0.17625
50%     0.23100
75%     0.28175
100%    0.50400
Name: 肝气郁结证型系数, dtype: float64
'''
d_f = pd.cut(dd_data, w, labels=range(k))
#print(d_f)

#聚类离散化

