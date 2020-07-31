# DESC, NAME으로 추출한 태그와 평점간의 태그의 공집합을 만들어서 태그를 만들어보자. 
# https://github.com/lovit/KR-WordRank 태그는 이걸로 다 뽑는건가.
from utils.util import removeBlank 
import matplotlib.pyplot as plt
from krwordrank.word import KRWordRank
from wordcloud import WordCloud
desc = open("./desc.txt", "r", encoding="utf-8").read().split('.')
name = open("./name.txt", "r", encoding="utf-8").read().split('.')
evaluation = open("./eval.txt", "r", encoding="utf-8").read().split('.')
scrap = open("./scrap_desc.txt", "r", encoding="utf-8").read().split('.')

texts = removeBlank(scrap)

min_count = 5   # 단어의 최소 출현 빈도수 (그래프 생성 시)
max_length = 10 # 단어의 최대 길이
wordrank_extractor = KRWordRank(min_count=min_count, max_length=max_length)

beta = 0.85    # PageRank의 decaying factor beta
max_iter = 10 
keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

print(keywords)
for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
        print('%8s:\t%.4f' % (word, r)) 

stopwords = {'너무', '좋다', '감사', '작가', '있다', '있는'} # 쓸데없는거 거르자. 
passwords = {word:score for word, score in sorted(
    keywords.items(), key=lambda x:-x[1])[:300] if not (word in stopwords)} 

print(passwords) 