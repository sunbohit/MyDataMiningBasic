import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

input_file = './consumption_data.xls'
output_file = './kmeans_result.xls'

cd_data = pd.read_excel(input_file, index_col = 'Id')
#print(cd_data)
'''
      R   F        M
Id                  
1    27   6   232.61
2     3   5  1507.11
3     4  16   817.62
4     3  11   232.81
5    14   7  1913.05
..   ..  ..      ...
938  19   4  1163.08
939   9   7  1007.06
940  27   7  1322.94
941  30   4   860.41
942  22   1   776.70

[940 rows x 3 columns]

'''
k = 3

epochs = 1000

#print(cd_data.mean())
'''
R      16.747872
F       9.615957
M    1061.683436
dtype: float64
'''
cd_data_norm = (cd_data-cd_data.mean())/cd_data.std()
#print(cd_data_norm)
'''
            R         F         M
Id                               
1    0.764186 -0.493579 -1.158711
2   -1.024757 -0.630079  0.622527
3   -0.950217  0.871423 -0.341103
4   -1.024757  0.188922 -1.158432
5   -0.204824 -0.357079  1.189868
..        ...       ...       ...
938  0.167872 -0.766579  0.141712
939 -0.577521 -0.357079 -0.076342
940  0.764186 -0.357079  0.365132
941  0.987804 -0.766579 -0.281299
942  0.391490 -1.176080 -0.398292

[940 rows x 3 columns]
'''
kmeans_model = KMeans(n_clusters=k, max_iter=epochs, n_jobs=4)
kmeans_model.fit(cd_data_norm)

#print(kmeans_model.labels_)
'''
[2 2 0 2 2 2 2 2 2 0 2 2 0 0 2 0 1 2 2 2 2 2 0 2 2 0 2 0 2 1 0 2 2 2 0 0 2
 2 0 2 2 0 2 2 0 2 2 2 0 0 2 2 2 0 2 2 2 1 2 2 2 0 0 2 0 2 2 2 2 2 0 0 2 2
 0 2 1 0 0 2 2 2 2 2 2 0 0 2 2 0 1 2 0 0 2 2 0 2 0 0 2 2 1 0 0 2 2 0 0 2 2
 0 2 2 2 1 2 2 1 0 2 2 2 2 2 2 2 2 2 1 2 2 2 2 2 2 2 2 1 2 2 2 2 0 2 2 2 2
 0 2 0 2 0 2 2 2 2 2 2 0 2 0 2 2 2 2 2 2 0 2 0 0 0 0 2 2 2 2 0 2 0 2 2 2 2
 0 2 2 0 2 2 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 0 0 2 2 2 2 0 2 2 0
 2 2 2 1 2 2 2 0 2 2 2 2 2 2 1 2 2 2 2 2 2 0 2 2 2 2 2 0 0 0 2 2 1 1 2 2 0
 2 2 0 2 2 0 2 0 2 1 2 2 2 2 0 0 0 2 0 2 2 2 1 2 2 2 2 0 0 2 2 0 2 2 2 2 2
 2 1 2 1 0 0 2 0 2 2 2 2 0 2 2 2 2 2 2 2 0 1 2 0 2 2 2 0 0 0 2 2 2 2 2 0 1
 2 0 0 2 0 0 0 2 2 2 2 0 2 2 2 2 0 2 2 2 0 2 0 1 0 2 2 2 0 0 2 0 2 2 0 2 2
 2 0 0 0 2 2 0 2 1 0 2 0 2 0 2 2 2 2 2 2 0 2 0 0 2 0 2 0 0 1 0 0 0 2 0 0 0
 0 2 0 2 0 0 2 0 0 0 2 1 2 2 0 2 0 0 2 2 0 0 0 2 2 2 0 0 2 0 2 0 2 0 0 2 0
 2 2 2 2 0 2 2 2 2 0 2 2 2 0 0 2 0 2 0 2 0 0 0 2 2 0 0 0 2 2 0 2 0 2 2 0 2
 0 0 0 2 2 2 2 2 2 2 0 0 0 0 2 2 0 2 0 2 0 2 2 2 2 2 0 2 0 0 2 0 0 2 0 2 0
 2 2 2 2 0 0 0 1 2 2 2 2 0 2 0 0 2 2 2 0 0 0 0 0 0 2 0 0 2 0 2 0 2 2 0 2 2
 0 2 0 1 2 0 2 2 2 0 2 2 0 0 2 2 0 0 2 0 2 0 0 2 0 2 0 2 2 2 0 2 2 2 0 2 2
 2 0 0 2 0 0 2 0 0 2 2 2 2 2 0 2 0 2 2 1 2 2 2 2 2 2 2 0 2 2 0 0 2 1 2 2 2
 0 0 0 2 2 0 0 0 2 2 2 1 0 0 0 2 2 2 2 2 0 2 0 2 1 0 0 2 2 0 2 2 2 2 0 2 0
 2 0 2 1 0 0 0 2 0 2 2 0 0 2 2 2 0 2 0 2 2 2 2 2 0 2 2 0 2 0 2 2 2 2 1 0 0
 2 2 0 2 0 2 2 0 2 2 2 0 0 2 2 2 2 1 0 0 2 2 2 2 0 0 2 0 2 2 0 0 2 2 1 2 2
 2 2 0 2 2 2 2 2 2 2 2 2 0 0 0 0 2 0 2 0 0 0 0 2 2 0 2 0 0 0 0 2 2 0 0 2 2
 0 2 0 0 2 2 2 2 2 2 0 2 0 2 1 2 1 0 2 0 2 0 0 0 0 2 0 2 0 0 2 0 2 2 2 2 2
 2 2 2 0 0 2 2 0 0 2 2 0 2 2 2 0 2 0 2 2 0 2 2 0 2 0 0 0 2 2 2 2 2 0 2 2 2
 2 2 2 2 2 0 0 2 2 0 0 2 2 0 2 0 0 0 2 2 0 0 1 0 0 0 0 0 2 2 1 0 0 0 2 2 0
 2 2 0 0 0 2 2 0 2 0 2 1 2 2 0 2 2 0 2 0 2 2 0 0 2 0 0 2 2 2 2 2 0 2 2 2 0
 2 0 0 0 0 2 0 0 0 2 2 2 2 2 2]
'''
#print(kmeans_model.cluster_centers_)
'''
[[-0.16295092  1.11672177  0.39557542]
 [ 3.45505486 -0.29565357  0.44912342]
 [-0.14785515 -0.65689153 -0.27225103]]
'''
s1 = pd.Series(kmeans_model.labels_)
#print(type(s1)) #<class 'pandas.core.series.Series'>
#print(s1)
'''
0      1
1      1
2      0
3      1
4      1
      ..
935    1
936    1
937    1
938    1
939    1
dtype: int32
'''
s1 = s1.value_counts()
#print(type(s1)) #<class 'pandas.core.series.Series'>
#print(s1)
'''
1    559
0    341
2     40
dtype: int64
'''
r1 = pd.DataFrame(kmeans_model.cluster_centers_)
#print(r1)
'''
          0         1         2
0  3.455055 -0.295654  0.449123
1 -0.160058  1.090294  0.402638
2 -0.149460 -0.665935 -0.286382
'''
row1 = pd.concat([r1,s1], axis=1)
#print(row1)
'''
          0         1         2    0
0  3.455055 -0.295654  0.449123   40
1 -0.149353 -0.658893 -0.271780  559
2 -0.160451  1.114802  0.392844  341
'''


#print(cd_data.index)
'''
Int64Index([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,
            ...
            933, 934, 935, 936, 937, 938, 939, 940, 941, 942],
           dtype='int64', name='Id', length=940)
'''
#print(pd.Series(kmeans_model.labels_, index=cd_data.index))
'''
Id
1      0
2      0
3      1
4      0
5      0
      ..
938    0
939    0
940    0
941    0
942    0
dtype: int32
'''
row2 = pd.concat([cd_data, pd.Series(kmeans_model.labels_, index=cd_data.index)],axis=1)
#print(row2)
'''
      R   F        M  0
Id                     
1    27   6   232.61  2
2     3   5  1507.11  2
3     4  16   817.62  0
4     3  11   232.81  2
5    14   7  1913.05  2
..   ..  ..      ... ..
938  19   4  1163.08  2
939   9   7  1007.06  2
940  27   7  1322.94  2
941  30   4   860.41  2
942  22   1   776.70  2

[940 rows x 4 columns]
'''

#print(row2.columns) #Index(['R', 'F', 'M', 0], dtype='object')
row2.columns = list(cd_data.columns)+['聚类类别']
#print(row2.columns) #Index(['R', 'F', 'M', '聚类类别'], dtype='object')

#print(row2)
'''
      R   F        M  聚类类别
Id                        
1    27   6   232.61     0
2     3   5  1507.11     0
3     4  16   817.62     1

4     3  11   232.81     0
5    14   7  1913.05     0
..   ..  ..      ...   ...
938  19   4  1163.08     0
939   9   7  1007.06     0
940  27   7  1322.94     0
941  30   4   860.41     0
942  22   1   776.70     0

[940 rows x 4 columns]
'''

row2.to_excel(output_file)

def density_plot(data): 
	p = data.plot(kind='kde', linewidth = 2, subplots = True, sharex = False)
	[p[i].set_ylabel('密度') for i in range(k)]
	plt.legend()
	return plt

pic_output = 'pd_' 
for i in range(k):
 	density_plot(cd_data[row2['聚类类别']==i]).savefig('%s%s.png' %(pic_output, i))
plt.show()

from sklearn.manifold import TSNE

tsne = TSNE()
tsne.fit_transform(cd_data_norm)
tsne = pd.DataFrame(tsne.embedding_, index=cd_data_norm.index)

d = tsne[row2['聚类类别'] == 0]
plt.plot(d[0], d[1], 'r.')
d = tsne[row2['聚类类别'] == 1]
plt.plot(d[0], d[1], 'go')
d = tsne[row2['聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')
plt.show()

