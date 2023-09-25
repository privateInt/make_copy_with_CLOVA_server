# make_copy_with_CLOVA_server

naver hyper clova API를 통해 광고카피를 생성하는 서버입니다.

flask, docker로 제작되었습니다.

# 사용법

- host, api_key, api_key_primary_val, request_id를 수정

- pip install -r requirements.txt
- python final_hyper_clova_flask.py
또는
- docker build -t 생성할REPOSITORY:생성할TAG Dockerfile이 있는 directory경로
- docker run -p 8066:8066 -it IMAGE ID (포트 8066, 변경가능)

# API 명세서
 - method: POST
 - port: 8066
 - endpoint: NCopy
 - Request Responses example
 - 
<Response [200]>

input: json{

"type": "head" or "body",

"name": "상품명",

"key": "키워드",

"tone": type이 head인 경우 "기본" or "리뷰" or "행동촉구" or "질문" or "언어유희", type이 body인 경우 "기본" or "리뷰" or "행동촉구"

}

output: json{

'input_dict': {'type': 'head', 'name': '썬크림', 'key': '끈적이지 않는,1+1', 'tone': '기본'},

'token_used': {'input': 453, 'output': 27, 'total_cost': 21.12},

'output': '백탁현상 없는 산뜻한 썬크림 1+1 행사중! 끈적이지 않아 남성분들도 부담없이 사용하실 수 있어요~'

}
