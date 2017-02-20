'''
从用tab分割的文本中读取数据(split方法)
'''
datafile = 'data_2.tab'

with open(datafile, 'r') as f:
	for line in f:
		print('未用strip()处理: ', line.split('\t'))
		# 去掉首位空白
		line = line.strip() 
		# now we split the line by tab delimiter
		print('经过strip()处理: ', line.split('\t'))  
'''
未用strip()处理:  ['"day"   "ammount"\n']
经过strip()处理:  ['"day"   "ammount"']
未用strip()处理:  ['2013-01-24  323 \n']
经过strip()处理:  ['2013-01-24  323']
未用strip()处理:  ['2013-01-25  233 \n']
经过strip()处理:  ['2013-01-25  233']
未用strip()处理:  ['2013-01-26  433\n']
经过strip()处理:  ['2013-01-26  433']
未用strip()处理:  ['2013-01-27  555\n']
经过strip()处理:  ['2013-01-27  555']
未用strip()处理:  ['2013-01-28  123\n']
经过strip()处理:  ['2013-01-28  123']
未用strip()处理:  ['    2013-01-29    0\n']
经过strip()处理:  ['2013-01-29    0']
未用strip()处理:  ['2013-01-30  221\n']
经过strip()处理:  ['2013-01-30  221']

'''