'''
应用scipy库进行拉格朗日插值法
'''

import pandas as pd
from scipy.interpolate import lagrange

inputfile = 'catering_sale.xls' #数据集
outputfile = 'catering_sale_lagrange.xls' #输出结果路径

cs_data = pd.read_excel(inputfile,index_col='日期')  #日期作为索引
cs_data['销量'][(cs_data['销量']>5000)|(cs_data['销量']<400)] = None #将所有异常值作为空值处理

def lagrange_model(column,n,k):
	#column为需要处理的列向量， n为被插值的位置， k为取前后的数据的个数

	#print(column)
	#print(n)
	#print(k)
	f_x = column[list(range(n-k,n))+list(range(n+1,n+k+1))] #取数
	f_x_index = list(range(n-k,n))+list(range(n+1,n+k+1))
	f_x = f_x[f_x.notnull()] # 剔除空值
	print(f_x)
	sub = 0
	for nn in f_x.notnull():
		if(not nn):
			del f_x_index[sub]
	print(f_x_index)
	print(list(f_x))
	return lagrange(f_x_index,list(f_x))(n) #应用拉格朗日差值法

print(cs_data.columns) # Index(['销量'], dtype='object')
print(len(cs_data)) # 201

for i in cs_data.columns:
	for j in range(len(cs_data)):
		#print(cs_data[i])
		#print(cs_data[i].isnull())
		#print(cs_data[i].isnull()[j])
		if(cs_data[i].isnull()[j]):
			cs_data[i][j] = lagrange_model(cs_data[i],j,5) 

cs_data.to_excel(outputfile)
print(cs_data)
