'''
应用pandas和matplotlib进行离群点检测
'''
import pandas as pd
import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei']
#plt.rcParams['axes.unicode_minus'] = False

cs_path = 'catering_sale.xls' # 数据集路径
cs_data = pd.read_excel(cs_path,index_col='日期') # 用pandas读入excel数据，将日期作为索引
print(cs_data)
print(type(cs_data))

plt.figure()
p = cs_data.boxplot()

print(type(p))
print(p)

plt.show()
