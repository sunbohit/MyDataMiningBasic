'''
从硬盘以流的形式将语料库加载至内存
'''

from gensim import corpora

dictionary = corpora.Dictionary() #创建字典对象
dictionary = dictionary.load('deerwester.dict') #加载字典
#print(dictionary.token2id)
'''
{'computer': 0, 'trees': 9, 'interface': 2, 'system': 6, 'survey': 5, 'graph': 10, 'eps': 8, 'human': 1, 'user': 3, 'minors': 11, 'time': 4, 'response': 7}
'''
class MyCorpus(object):
	def __iter__(self):
		for line in open('mycorpus.txt'):
			# 假设每行是一个文档，词都以空格为间隔
			yield dictionary.doc2bow(line.lower().split())

corpus_memory_friendly = MyCorpus()  # 没有直接将语料库放入内存
#print(corpus_memory_friendly) #<__main__.MyCorpus object at 0x7fa9e58a7780>

for vector in corpus_memory_friendly:  # 每次只将一个向量载入内存
	print(vector)
'''
[(0, 1), (1, 1), (2, 1)]
[(0, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
[(2, 1), (3, 1), (6, 1), (8, 1)]
[(1, 1), (6, 2), (8, 1)]
[(3, 1), (4, 1), (7, 1)]
[(9, 1)]
[(9, 1), (10, 1)]
[(9, 1), (10, 1), (11, 1)]
[(5, 1), (10, 1), (11, 1)]
'''
