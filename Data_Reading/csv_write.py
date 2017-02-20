'''
写入csv文件
'''
import csv #载入csv模块

filename = 'data_write.csv' #写入路径

# 以可写方式打开文件
with open(filename,'w') as f:
    writer = csv.writer(f)
    for row in range(10):
        writer.writerow([row + 1, '2012-01-%s' % (19 + row)]) 
