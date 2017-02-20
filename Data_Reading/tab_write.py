'''
输出用tab分割的文本
'''
import csv

filename = 'data_write.tab'

# 以普通可写方式打开文件
with open(filename,'w') as f:
    writer = csv.writer(f, dialect=csv.excel_tab)
    for row in range(10):
        writer.writerow([row + 1, '2017-01-%s' % (19 + row)]) 
