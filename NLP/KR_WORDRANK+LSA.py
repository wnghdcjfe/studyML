# DESC, NAME으로 추출한 태그와 평점간의 태그의 공집합을 만들어서 태그를 만들어보자. 
# https://github.com/lovit/KR-WordRank 태그는 이걸로 다 뽑는건가.
from utils.util import removeBlank 
import matplotlib.pyplot as plt
from krwordrank.word import KRWordRank
from wordcloud import WordCloud
 
from gensim import corpora
from gensim.models import LsiModel
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim.models.coherencemodel import CoherenceModel
import matplotlib.pyplot as plt

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

dictlist = []
for key, value in passwords.items(): 
    dictlist.append(key) 

print(dictlist)
def prepare_corpus(doc_clean):
    """
    Input  : clean document
    Purpose: create term dictionary of our courpus and Converting list of documents (corpus) into Document Term Matrix
    Output : term dictionary and Document Term Matrix
    """
    # Creating the term dictionary of our courpus, where every unique term is assigned an index. dictionary = corpora.Dictionary(doc_clean)
    dictionary = corpora.Dictionary(doc_clean)
    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    # generate LDA model
    return dictionary,doc_term_matrix
    
def create_gensim_lsa_model(doc_clean,number_of_topics,words):
    """
    Input  : clean document, number of topics and number of words associated with each topic
    Purpose: create LSA model using gensim
    Output : return LSA model
    """
    dictionary,doc_term_matrix=prepare_corpus(doc_clean)
    # generate LSA model
    lsamodel = LsiModel(doc_term_matrix, num_topics=number_of_topics, id2word = dictionary)  # train model
    print(lsamodel.print_topics(num_topics=number_of_topics, num_words=words))
    return lsamodel

number_of_topics=7
words=10
model=create_gensim_lsa_model(dictlist,number_of_topics,words)
