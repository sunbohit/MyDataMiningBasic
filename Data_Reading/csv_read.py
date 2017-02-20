'''
从CSV文件中导入数据
'''
import csv #导入csv模块

filename = 'data.csv' #数据集路径

data = []
try:
    with open(filename) as f: # 获得文件对象
        reader = csv.reader(f) # 用csv模块读取文件
        c = 0
        for row in reader: #可以使用for...in...来遍历csv文档
            if c == 0:
                header = row #第一次读入的行是列表的header
            else:
                data.append(row) #将数据存入data列表
            c += 1
except csv.Error as e:
    print("Error reading CSV file at line %s: %s" % (reader.line_num, e)) #打印异常
    sys.exit(-1)

if header:
    print(header)
    print('==================')

for datarow in data:
    print(datarow)
'''
['day', 'ammount']
==================
['2013-01-24', '323']
['2013-01-25', '233']
['2013-01-26', '433']
['2013-01-27', '555']
['2013-01-28', '123']
['2013-01-29', '0']
['2013-01-30', '221']
'''
