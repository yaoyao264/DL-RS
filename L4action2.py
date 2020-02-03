# =============================================================================
# from snownlp import SnowNLP
# 
# text=open('F:/ZOOM/人工智能/推荐系统与机器学习课件/推荐系统与机器学习作业/RS6-master/L4/textrank/news.txt')
# t=text.read()
# 
# snow = SnowNLP(t)
# 
# print(snow.keywords(20))
# 
# print(snow.summary(8))
# =============================================================================


from textrank4zh import TextRank4Keyword, TextRank4Sentence

text=open('F:/ZOOM/人工智能/推荐系统与机器学习课件/推荐系统与机器学习作业/RS6-master/L4/textrank/news.txt')
t=text.read()

tr4w=TextRank4Keyword()
tr4w.analyze(text=t,lower=False,window=3)
print('关键词：')
for item in tr4w.get_keywords(50,word_min_len=2):
    print(item.word,end='  '),

tr4s=TextRank4Sentence()
tr4s.analyze(text=t,lower=False,source='all_filters')
print('\n摘要:')
for item in tr4s.get_key_sentences(num=5):
    print(item.sentence,end='')


# =============================================================================
# import jieba
# import jieba.analyse
# import jieba.posseg as pseg
# 
# text=open('F:/ZOOM/人工智能/推荐系统与机器学习课件/推荐系统与机器学习作业/RS6-master/L4/textrank/news.txt')
# t=text.read()
# 
# seg_list=jieba.cut(t,cut_all=False)
# print(' '.join(seg_list))
# 
# words=pseg.cut(t)
# for word,flag in words:
#     print('%s,%s'%(word,flag))
# 
# keywords=jieba.analyse.extract_tags(t,topK=25,withWeight=False,allowPOS=('n','nr','ns'))
# for item in keywords:
#     print(item[0],item[1])
# print('-'*100)
# 
# 
# keywords = jieba.analyse.extract_tags(t, topK=20, withWeight=True, allowPOS=('n','nr','ns'))
# keywords = jieba.analyse.textrank(t, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v')) 
# keywords = jieba.analyse.textrank(t, topK=20, withWeight=True, allowPOS=('n', 'ns')) 
# keywords = jieba.analyse.textrank(t, topK=20, withWeight=True) 
# print(keywords)
# for item in keywords:
#     print(item[0],item[1])
# =============================================================================
