'''
应用pandas和matplotlib进行离群点检测
'''
import pandas as pd
import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei']
#plt.rcParams['axes.unicode_minus'] = False

cs_path = 'catering_sale.xls'
cs_data = pd.read_excel(cs_path,index_col='日期')
#print(cs_data)
print(type(cs_data))
plt.figure()
p = cs_data.boxplot()

print(type(p))
print(p)

plt.show()