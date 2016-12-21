import pandas as pd

datafile = 'catering_sale.xls'
cs_data = pd.read_excel(datafile, index_col = '日期')
cs_data = cs_data[(cs_data['销量']>400)&(cs_data['销量']<5000)]
stat = cs_data.describe()

print(stat)

'''
                销量
count   195.000000
mean   2744.595385
std     424.739407
min     865.000000
25%    2460.600000
50%    2655.900000
75%    3023.200000
max    4065.200000
'''
stat.loc['极差'] = stat.loc['max'] - stat.loc['min']
stat.loc['变异系数'] = stat.loc['std'] / stat.loc['mean']
stat.loc['四分位间距'] = stat.loc['75%'] - stat.loc['25%']

print(stat)

'''
                销量
count   195.000000
mean   2744.595385
std     424.739407
min     865.000000
25%    2460.600000
50%    2655.900000
75%    3023.200000
max    4065.200000
极差     3200.200000
变异系数      0.154755
四分位间距   562.600000
'''
