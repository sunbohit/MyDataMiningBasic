from gensim import corpora

corpus = [[(1, 0.5)], [(4, 0.3)], []]

corpora.MmCorpus.serialize('corpus.mm', corpus) # Market Matrix format
corpora.SvmLightCorpus.serialize('corpus.svmlight', corpus) # Joachim’s SVMlight format
corpora.BleiCorpus.serialize('corpus.lda-c', corpus) #  Blei’s LDA-C format
corpora.LowCorpus.serialize('corpus.low', corpus) # GibbsLDA++ format

# load a corpus
corpus_2 = corpora.MmCorpus('corpus.mm')
print(corpus_2)
# MmCorpus(3 documents, 5 features, 2 non-zero entries)
'''
'''
# 1
print(list(corpus_2))
'''
[[(1, 0.5)], [(4, 0.3)], []]
'''
# 2 better
for doc in corpus_2:
	print(doc)
'''
[(1, 0.5)]
[(4, 0.3)]
[]
'''
