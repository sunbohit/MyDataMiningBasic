'''
pandas 可以读取excel文件，并自动生成数据的分析描述
'''
import pandas as pd
datafile = 'catering_sale.xls'
cs_data = pd.read_excel(datafile, index_col = '日期')
print(cs_data.describe())
'''
           销量
count   200.000000
mean   2755.214700
std     751.029772
min      22.000000
25%    2451.975000
50%    2655.850000
75%    3026.125000
max    9106.440000

'''