from flask import Flask, jsonify, request
import base64
import sys
import os
sys.path.append(os.getcwd())
from final_hyper_clova_utils import *

app = Flask(__name__)

info_dict = make_info_dict()

basic_head_completion_executor = make_CompletionExecutor(info_dict, "head", "basic")
review_head_completion_executor = make_CompletionExecutor(info_dict, "head", "review")
callforaction_head_completion_executor = make_CompletionExecutor(info_dict, "head", "CallForAction")
question_head_completion_executor = make_CompletionExecutor(info_dict, "head", "question")
languagepaly_head_completion_executor = make_CompletionExecutor(info_dict, "head", "LanguagePlay")
basic_body_completion_executor = make_CompletionExecutor(info_dict, "head", "basic")
review_body_completion_executor = make_CompletionExecutor(info_dict, "head", "review")
callforaction_body_completion_executor = make_CompletionExecutor(info_dict, "head", "CallForAction")


request_data = make_request_data()

@app.route('/NCopy', methods=['POST'])
def NCopy():
    # default 정보 저장
    data_type = "head"
    data_name = "썬크림"
    data_key = "끈적이지 않는,1+1"
    data_tone = "행동촉구"
    
    # 데이터 받기
    data_dict = json.loads(request.data)
    
    # 받은 데이터 정보를 저장
    if "type" in data_dict:
        data_type = data_dict["type"]
    if "name" in data_dict:
        data_name = data_dict["name"]
    if "key" in data_dict:
        data_key = data_dict["key"]
    if "tone" in data_dict:
        data_tone = data_dict["tone"]

    # 받은 데이터 정보로 request요청 보낼 형식 작성
    if data_type == "head":
        target = make_head_example(data_name, data_key, data_tone)
        request_data["text"] = target
        request_data["maxTokens"] = 100
        if data_tone == "기본":
            response = basic_head_completion_executor.execute(request_data)
        elif data_tone == "리뷰":
            response = review_head_completion_executor.execute(request_data)
        elif data_tone == "행동촉구":
            response = callforaction_head_completion_executor.execute(request_data)
        elif data_tone == "질문":
            response = question_head_completion_executor.execute(request_data)
        elif data_tone == "언어유희":
            response = languagepaly_head_completion_executor.execute(request_data)
    else:
        target = make_body_example(data_name, data_key, data_tone)
        request_data["text"] = target
        request_data["maxTokens"] = 300
        if data_tone == "기본":
            response = basic_body_completion_executor.execute(request_data)
        elif data_tone == "리뷰":
            response = review_body_completion_executor.execute(request_data)
        elif data_tone == "행동촉구":
            response = callforaction_body_completion_executor.execute(request_data)
    
    # request요청 보내 받은 response값을 뿌려주기 좋게 형식변경
    return_dict = {}
    return_dict['input_dict'] = {"type": data_type, "name": data_name, "key": data_key, "tone": data_tone}
    return_dict['token_used'] = {"input": response['result']['inputLength'], "output": response['result']['outputLength'], "total_cost": round((response['result']['inputLength'] + response['result']['outputLength'])*0.044, 3)}
    return_dict['output'] = response['result']['text'].replace(target,"")
    
    # response_text = response_text.replace(target,"").replace("#","").replace("\"","")
    print(f"type: {data_type}")
    print(f"name: {data_name}")
    print(f"key: {data_key}")
    print(f"tone: {data_tone}")
    print(response['result']['text'].replace(target,""))
    request_data["text"] = ""
    
    return json.dumps(return_dict, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8066)