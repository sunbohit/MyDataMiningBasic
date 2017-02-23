'''
gensim的简单使用
'''
from gensim import corpora, models, similarities
import jieba

# 创建含有3个句子的语料库
sentences = ["马上就到元旦了","香蕉是很好吃且含糖量很高的水果","它不喜欢吃普通的狗粮，它想吃水果"]

words=[]
for doc in sentences:
	words.append(list(jieba.cut(doc))) # 应用jieba分词进行分词并存储为列表的形式
print(words)
'''
[['马上', '就', '到', '元旦', '了'], ['香蕉', '是', '很', '好吃', '且', '含糖量', '很', '高', '的', '水果'], ['它', '不', '喜欢', '吃', '普通', '的', '狗', '粮', '，', '它', '想', '吃水果']]
'''

dic = corpora.Dictionary(words) # 应用Dictionary函数建立词典
print(dic)
'''
Dictionary(24 unique tokens: ['普通', '马上', '到', '狗', '不']...)
'''
print(dic.token2id) # 应用token2id为词典中的词编号，保存为python字典的形式
'''
{'普通': 14, '马上': 2, '到': 4, '狗': 19, '不': 15, '好吃': 12, '了': 0, '想': 22, '元旦': 3, '高': 6, '，': 18, '的': 11, '它': 23, '是': 9, '吃': 20, '香蕉': 10, '喜欢': 21, '水果': 13, '很': 5, '粮': 16, '含糖量': 8, '且': 7, '吃水果': 17, '就': 1}
'''
for word,index in dic.token2id.items(): #输出字典
	print(word," 编号为: ",index)
'''
普通  编号为:  14
马上  编号为:  2
到  编号为:  4
狗  编号为:  19
不  编号为:  15
好吃  编号为:  12
了  编号为:  0
想  编号为:  22
元旦  编号为:  3
高  编号为:  6
，  编号为:  18
的  编号为:  11
它  编号为:  23
是  编号为:  9
吃  编号为:  20
香蕉  编号为:  10
喜欢  编号为:  21
水果  编号为:  13
很  编号为:  5
粮  编号为:  16
含糖量  编号为:  8
且  编号为:  7
吃水果  编号为:  17
就  编号为:  1
'''
print(type(dic)) #<class 'gensim.corpora.dictionary.Dictionary'>
corpus = [dic.doc2bow(text) for text in words] #http://radimrehurek.com/gensim/corpora/dictionary.html 用bag-of-words词袋模型处理列表中的每个句子（将词替换为id，并计数）
print(corpus)
'''
[[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], [(5, 2), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1)], [(11, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 2)]]
'''
tfidf = models.TfidfModel(corpus) #http://radimrehurek.com/gensim/models/tfidfmodel.html 计算出TF-IDF模型

vec = [(16, 1), (14, 1),(8,1),(10,1)]
print(tfidf[vec]) #测试TF-IDF模型
'''
[(16, 0.5), (14, 0.5), (8, 0.5), (10, 0.5)]
'''

corpus_tfidf = tfidf[corpus] #TF-IDF变换，调整特征词的权值
for doc in corpus_tfidf:
    print(doc)
'''
[(0, 0.4472135954999579), (1, 0.4472135954999579), (2, 0.4472135954999579), (3, 0.4472135954999579), (4, 0.4472135954999579)]
[(5, 0.5993233993308021), (6, 0.29966169966540107), (7, 0.29966169966540107), (8, 0.29966169966540107), (9, 0.29966169966540107), (10, 0.29966169966540107), (11, 0.11059621734070547), (12, 0.29966169966540107), (13, 0.29966169966540107)]
[(11, 0.10182957857895131), (14, 0.27590839295322883), (15, 0.27590839295322883), (16, 0.27590839295322883), (17, 0.27590839295322883), (18, 0.27590839295322883), (19, 0.27590839295322883), (20, 0.27590839295322883), (21, 0.27590839295322883), (22, 0.27590839295322883), (23, 0.5518167859064577)]
'''

#index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=9)
#sims = index[tfidf[vec]]
#print(list(enumerate(sims)))

lsi = models.LsiModel(corpus_tfidf, id2word=dic, num_topics=2) #http://radimrehurek.com/gensim/models/lsimodel.html LSI模型，设定主题数为2
lsiout=lsi.print_topics(2)
print(lsiout[0])
print(lsiout[1])
'''
(0, '0.421*"很" + 0.388*"它" + 0.211*"高" + 0.211*"且" + 0.211*"香蕉" + 0.211*"好吃" + 0.211*"水果" + 0.211*"是" + 0.211*"含糖量" + 0.194*"粮"')
(1, '0.447*"就" + 0.447*"到" + 0.447*"元旦" + 0.447*"了" + 0.447*"马上" + -0.000*"它" + -0.000*"粮" + -0.000*"不" + -0.000*"吃" + -0.000*"想"')
'''
corpus_lsi = lsi[corpus_tfidf] #用LSI模型转换原始文本
for doc in corpus_lsi: 
	print( doc )
'''
[(1, 1.0)]
[(0, 0.71107733974729614)]
[(0, 0.71107733974732845)]
'''

lda = models.LdaModel(corpus_tfidf, id2word=dic, num_topics=2) #http://radimrehurek.com/gensim/models/ldamodel.html LDA模型 主题数为2
ldaOut=lda.print_topics(2)
print(ldaOut[0])
print(ldaOut[1])
'''
(0, '0.060*"很" + 0.050*"它" + 0.046*"高" + 0.046*"且" + 0.046*"是" + 0.045*"水果" + 0.045*"香蕉" + 0.045*"含糖量" + 0.043*"好吃" + 0.041*"不"')
(1, '0.057*"就" + 0.056*"马上" + 0.056*"到" + 0.056*"元旦" + 0.056*"了" + 0.046*"它" + 0.039*"普通" + 0.039*"吃" + 0.039*"喜欢" + 0.039*"粮"')
'''
corpus_lda = lda[corpus_tfidf]
for doc in corpus_lda:
	print(doc)
'''
[(0, 0.1769723209123639), (1, 0.82302767908763619)]
[(0, 0.8341907935689955), (1, 0.16580920643100444)]
[(0, 0.77661637409701878), (1, 0.22338362590298108)]
'''

index = similarities.MatrixSimilarity(lsi[corpus])
query = "香蕉"
query_bow = dic.doc2bow(list(jieba.cut(query)))
print(query_bow) #[(10, 1)]
query_lsi = lsi[query_bow]
print(query_lsi)
'''
[(0, 0.21070963938457199)]
'''
