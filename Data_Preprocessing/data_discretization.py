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
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=k)
#print(dd_data)
reshape_data = dd_data.values.reshape((len(dd_data),1))
#print(reshape_data)
kmeans_model.fit(reshape_data)
#print(kmeans_model.labels_)
#c = pd.DataFrame(kmeans_model.labels_)
#print(c) #所得标签并不符合小标签对应小类的序数关系
cent = pd.DataFrame(kmeans_model.cluster_centers_).sort_values(0)
#print(cent)
'''
          0
2  0.136954
0  0.220441
1  0.295007
3  0.408679
'''
w = cent.rolling(center=False,window=2).mean()
#print(w)
'''
          0
2       NaN
1  0.178698
3  0.257724
0  0.351843
'''
w = w.iloc[1:]
w = [0] + list(w[0]) + [dd_data.max()]
#print(w)
'''
[0, 0.17869758895131088, 0.25772406433683875, 0.35184318136037063, 0.504]
'''
d_c = pd.cut(dd_data, w, labels = range(k))
#print(d_c)

#可视化
import matplotlib.pyplot as  plt
def cluster_plot(d, k):
	plt.figure(figsize = (8,3))
	for j in range(k):
		plt.plot(dd_data[d==j], [j for i in d[d==j]], 'o')
	plt.ylim(-0.5,k-0.5)
	plt.show()
	return
cluster_plot(d_w, k)
cluster_plot(d_f, k)
cluster_plot(d_c, k)
	
