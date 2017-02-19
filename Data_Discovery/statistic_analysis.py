'''
应用pandas进行统计量分析，包括自定义统计量。
'''
import pandas as pd

datafile = 'catering_sale.xls' #数据集路径
cs_data = pd.read_excel(datafile, index_col = '日期') #以日期为索引读入数据框
cs_data = cs_data[(cs_data['销量']>400)&(cs_data['销量']<5000)] #过滤掉异常数据
stat = cs_data.describe() #输出pandas基本统计量

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
stat.loc['极差'] = stat.loc['max'] - stat.loc['min'] #极差是最大最小值间的差值
stat.loc['变异系数'] = stat.loc['std'] / stat.loc['mean'] # 变异系数用来衡量离中趋势
stat.loc['四分位间距'] = stat.loc['75%'] - stat.loc['25%'] # 四分位间距也是用来衡量离中程度，具有跟很好的鲁棒性

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
