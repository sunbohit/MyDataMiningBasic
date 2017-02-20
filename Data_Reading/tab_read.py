'''
从用tab分割的文本中读取数据(csv方法)
'''
import csv

filename = 'data.tab'

data = []
try:
    with open(filename) as f:
        reader = csv.reader(f, dialect=csv.excel_tab) #设定分隔符为tab
        c = 0
        for row in reader:
            if c == 0:
                header = row #首行为header
            else:
                data.append(row)
            c += 1
except csv.Error as e:
    print("Error reading CSV file at line %s: %s" % (reader.line_num, e)) #异常输出
    sys.exit(-1)

if header:
    print(header)
    print('===================')

for datarow in data:
    print(datarow)
'''
['day   "ammount"']
===================
['2013-01-24  323']
['2013-01-25  233']
['2013-01-26  433']
['2013-01-27  555']
['2013-01-28  123']
['2013-01-29    0']
['2013-01-30  221']['day   "ammount"']
===================
['2013-01-24  323']
['2013-01-25  233']
['2013-01-26  433']
['2013-01-27  555']
['2013-01-28  123']
['2013-01-29    0']
['2013-01-30  221']
'''
