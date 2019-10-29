# gbj  

<<< 여행지 챗봇 >>>    
    
@개발 환경
1. Windows 10  
2. Python 3.7.3  
3. Android studio

### intent_classification.py
- 워드 임베딩, 의도파악 학습 후 모델에 적용 >> 의도 분류

### entity_classification.py
- 워드임베딩, 개체명인식 학습 후 모델에 적용 >> 개체명 분류

### seq2seq_translation.py
- 워드임베딩, seq2seq 학습 후 모델에 적용 >> seq2seq 대화

### image_analysis.py
- 이미지 학습 후 모델에 적용 >> 이미지 분류

### application.py
- 챗봇 로직(의도파악, 개체명인식, fallback, seq2seq, 이미지분석, 시나리오(웹 크롤링))

### scenario.py
- 각 의도 웹 크롤링 실행

1. intent 확인 후 맞는 카테고리 메소드 실행
2. 테그 분리 후 크롤링 실행

<br>
<br>

### Flask_restfulAPI.py
- flask_restful api 사용
- POST방식으로 온 json 데이터를 파싱 후 훈련된 모델에 넣어 결과값 예측 후 클라이언트에게 결과값 리턴

<br>
<br>
<br>
<br>

# 실행방법
<br>

--- configs 파일 root_path 수정 (경로 다를 경우)
--- model_configs 파일 root_path 수정 (경로 다를 경우)


@실행 방법
1) flaskrestful.py를 실행합니다.(맨 마지막 라인 port는 자신의 포트 번호로 바꿔준다.)  
2) 압축된 TravelChat_v2-master_8 파일을 풀어서 켠 후, app/java/com.hoingmarry.travelchat/ChatActivity 파일에서 Ctrl + F로 192.168.0 검색 후, 192.168.0.내 IP:포트 번호  
로 고쳐준다.(이 때, flaskrestful.py 의 포트 번호와 일치할 것) 그리고 나서 앱을 실행한다.  

3) 여행 정보나 맛집, 날씨, 미세먼지 등의 정보를 알 수 있다.
ex) User: 서울 맛집  --- Chatbot: 어떤 음식으로 알려드릴까요?
  User: 치킨 --- Chatbot: 답변~  

여행지 알려줘, 광명 날씨...  
  
메시지 입력 창 옆에 클립 선택 시, 이미지 선택을 할 수 있다. 여기에 들어가는 이미지는 
약 27개의 관광지를 분류해놓았다. 가능한 곳은 안압지, 첨성대, 백록담 등... test/image_guide.csv에 목록이 있다. 데이터는 따로 DB에 담아놓았다.