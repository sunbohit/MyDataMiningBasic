import pandas as pd
from sklearn.cluster import KMeans

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
print(cd_data_norm)
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




