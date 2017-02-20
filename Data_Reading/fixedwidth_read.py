'''
从有固定格式的文本中用模板读取数据
'''

import struct
import string

mask='9s14s5s' #模板，对应每一行
parse = struct.Struct(mask).unpack_from
print('formatstring {!r}, record size: {}'.format(mask, struct.calcsize(mask)))

datafile = 'fixed-width.data' #文件路径

with open(datafile, 'rb') as f: #需要以二进制形式打开文件
    for line in f:
        fields = parse(line) #解析
        print('fields: ', [field.strip() for field in fields])

