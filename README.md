# studyML 
for study for ML for DL

# 추천시스템
태그기반으로 유사도를 측정해 최적의 작품 또는 전시회를 추천해주자. 

## 작품 - 그라폴리오를 기준으로
작가가 붙인 태그
https://grafolio.naver.com/works/1605097
 - 예쁜
 - 일러스트레이터
 - 그라폴리오
 - 회화
 - 그림

댓글을 활용할 수 있을까? 

작품에 대한 평점이 거의 없는데.. 

## 전시회 - 다 찾아보자~
전시회 관련태그는 정해진게 없음. 전시회를 설명하는 기본 설명, 전시회에 대한 정보를 스크래핑해서 얻는 정보 + 전시회 댓글 정보들로 태그를 정할 수 있음
 - KRWordRank 로 문장에서 TOP5의 단어를 기본으로 태그 선정가능 

## 유사도기법
 - LSA(Latent Semantic Analysis) - https://www.youtube.com/watch?v=OvzJiur55vo
 - LDA(Latent Dirichlet Allocation)
 - cosine similarity
 - glove(https://github.com/stanfordnlp/GloVe)
 - word2Vec

## LSA가 과연 맞을까? 
LSA는 말뭉치 전체의 통계 정보를 활용하지만 결과물에서 단어/문서 간의 유사도를 측정하기는 어렵다. 한편 Word2Vec는 단어 벡터 사이이의 유사도를 측정하는 데 좋지만 윈도우 크기 내에서만 학습이 이루어지기 때문에 말뭉치 전체에서의 등장 정보 (co-occurence)를 얻을 수 없다. GloVe는 이 둘의 약점을 보완하여 단어 벡터 간 유사도 측정이 수월하면서도 말뭉치 전체의 통계 정보를 잘 반영하기 위해 새로운 목적함수를 정의하였다.

## 영감
https://arena.kakao.com/forum/topics/295 
 - 댓글의 수가 적은 표본은 버릴까? 
 - XG boost 모델? 
 - AutoEncoder(https://arxiv.org/pdf/1708.01715.pdf)
 - Item2Vec
 - LDA와 Word2Vec을 결합한 Ida2vec
 - KNN?

http://tech.opentable.com/2015/08/11/navigating-themes-in-restaurant-reviews-with-word-movers-distance/

## 작품에 대한 태그생성
 - Triplet Network
 참고 논문: http://smedia.ust.hk/james/projects/deepart_project/frp667-maoA.pdf
 참고 코드: https://github.com/adambielski/siamese-triplet


## 수민앙?
초기 rating data 가 필요.??

## Similarity User Recommendation
나중에 유저 정보들이 확정되면..?  
협업필터링 - surprise (http://machinelearningkorea.com/2019/05/18/surprise-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%98%91%EC%97%85%ED%95%84%ED%84%B0%EB%A7%81collaborative-filtering-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%B9%98/)

## 고민 
전시회 태그잡기는 전시회설명 + 전시회를 간 리뷰 + 전시회를 키워드로 서칭했을 때 뜨는 뉴스나 관련 블로그 글을 정보로?

## 아니 링크가 사라진다니 무슨 말이오. 
여기에 전시회 리뷰가 잘 담기는데 https://booking.naver.com/booking/12/bizes/286064 전시회가 끝나면 이 링크에 접근 불가.. 누적값을 찾을 수 있는 방법은 없을까?  

작품관람을 클릭하면 그 관람에 대한 리뷰들만을 볼 수 있다. 

어떠한 전시회를 등록했다면 거기에 대한 뉴스, 블로그글을 모조리 스크래핑해서 거기에 있는 텍스트를 기반으로 태그를 잡아볼까? 그러면 작가도 모르는 태그가 잡힐 것이고 그 전시회를 간 사람에게 정확한 테스팅이 가능하지 않을까? 

## 네이버블로그 전시회 정보 가져올 때 팁
iframe으로 감싸져있는 것을 풀어야 한다. 
https://blog.naver.com/PostView.nhn?blogId=designpress2016&logNo=221469663565&redirect=Dlog&widgetTypeCall=true&directAccess=false
iframe이라면 이런식으로 접근을 해서 해야 한다. 
`document.querySelector('.se-main-container').textContent`
이렇게 가져오면 끝
