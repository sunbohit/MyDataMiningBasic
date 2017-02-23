'''
将文本转化为向量
'''

from gensim import corpora

documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

#stoplist = set('for a of the and to in')
#print(stoplist) #{'r', 'h', 'n', 'd', ' ', 'f', 'e', 't', 'i', 'a', 'o'}

stoplist = set('for a of the and to in'.split()) #设置停用词
#print(stoplist) #{'in', 'of', 'the', 'and', 'a', 'to', 'for'}

# 过滤掉停用词并将词语统一为小写的形式
texts = [ [word for word in document.lower().split() if word not in stoplist] for document in documents]
#print(texts)
'''
[	['human', 'machine', 'interface', 'lab', 'abc', 'computer', 'applications'], 
	['survey', 'user', 'opinion', 'computer', 'system', 'response', 'time'], 
	['eps', 'user', 'interface', 'management', 'system'], 
	['system', 'human', 'system', 'engineering', 'testing', 'eps'], 
	['relation', 'user', 'perceived', 'response', 'time', 'error', 'measurement'], 
	['generation', 'random', 'binary', 'unordered', 'trees'], 
	['intersection', 'graph', 'paths', 'trees'], 
	['graph', 'minors', 'iv', 'widths', 'trees', 'well', 'quasi', 'ordering'], 
	['graph', 'minors', 'survey']]
'''

# 词频统计
from collections import defaultdict
frequency = defaultdict(int) #defaultdict(int)默认值是0
for text in texts:
	for token in text:
		frequency[token] += 1
#print(frequency)
'''
defaultdict(<class 'int'>, {'computer': 2, 'human': 2, 'trees': 3, 'engineering': 1, 'survey': 2, 'well': 1, 'system': 4, 'lab': 1, 'response': 2, 'binary': 1, 'applications': 1, 'widths': 1, 'random': 1, 'unordered': 1, 'user': 3, 'relation': 1, 'machine': 1, 'minors': 2, 'eps': 2, 'abc': 1, 'intersection': 1, 'measurement': 1, 'error': 1, 'management': 1, 'opinion': 1, 'interface': 2, 'graph': 3, 'quasi': 1, 'perceived': 1, 'testing': 1, 'paths': 1, 'ordering': 1, 'time': 2, 'generation': 1, 'iv': 1})
'''
# 过滤掉只出现了一次的词
texts = [[token for token in text if frequency[token] > 1] for text in texts]
#print(texts)
'''
[	['human', 'interface', 'computer'], 
	['survey', 'user', 'computer', 'system', 'response', 'time'], 
	['eps', 'user', 'interface', 'system'], 
	['system', 'human', 'system', 'eps'], 
	['user', 'response', 'time'], ['trees'], 
	['graph', 'trees'], 
	['graph', 'minors', 'trees'], 
	['graph', 'minors', 'survey']]
'''

#bag-of-words词袋模型
dictionary = corpora.Dictionary(texts) #建立词典
#print(type(dictionary)) #<class 'gensim.corpora.dictionary.Dictionary'>
dictionary.save('deerwester.dict') #保存词典
#print(dictionary) #Dictionary(12 unique tokens: ['computer', 'trees', 'survey', 'eps', 'system']...)
#print(dictionary.token2id) #为词典中的词语编号
'''
{'minors': 11, 'time': 4, 'computer': 0, 'interface': 2, 'human': 1, 'survey': 5, 'trees': 9, 'user': 3, 'response': 7, 'system': 6, 'eps': 8, 'graph': 10}
'''
new_doc = "Human computer interaction" #新语料
new_vec = dictionary.doc2bow(new_doc.lower().split())
#print(new_vec)  # 新词"interaction"没有出现在词典中，直接忽略掉
'''
[(0, 1), (1, 1)]
'''
corpus = [dictionary.doc2bow(text) for text in texts] # 用词袋模型处理整个语料库
corpora.MmCorpus.serialize('deerwester.mm', corpus)  # 保存至磁盘
#print(corpus)
'''
[	[(0, 1), (1, 1), (2, 1)], 
	[(0, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)], 
	[(2, 1), (3, 1), (6, 1), (8, 1)], 
	[(1, 1), (6, 2), (8, 1)], 
	[(3, 1), (4, 1), (7, 1)], 
	[(9, 1)], [(9, 1), (10, 1)], 
	[(9, 1), (10, 1), (11, 1)], 
	[(5, 1), (10, 1), (11, 1)]]
'''
