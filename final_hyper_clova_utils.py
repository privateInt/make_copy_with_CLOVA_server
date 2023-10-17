import base64
import json
import http.client


class CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def _send_request(self, completion_request):
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id
        }

        conn = http.client.HTTPSConnection(self._host)
        conn.request('POST', '/serviceapp/v1/completions/LK-D2', json.dumps(completion_request), headers)
        response = conn.getresponse()
        result = json.loads(response.read().decode(encoding='utf-8'))
        conn.close()
        return result

    def execute(self, completion_request):
        res = self._send_request(completion_request)
        if res['status']['code'] == '20000':
            return res
        else:
            return 'Error'
        
def make_info_dict():
    final_dict, head_dict, body_dict = {}, {}, {}
    head_dict["basic"] = {"host":'host1',
    "api_key":'api_key1',
    "api_key_primary_val":'api_key_primary_val1',
    "request_id":'request_id1'}

    head_dict["review"] = {"host":'host2',
    "api_key":'api_key2',
    "api_key_primary_val":'api_key_primary_val2',
    "request_id":'request_id2'}

    head_dict["CallForAction"] = {"host":'host3',
    "api_key":'api_key3',
    "api_key_primary_val":'api_key_primary_val3',
    "request_id":'request_id3'}

    head_dict["question"] = {"host":'host4',
    "api_key":'api_key4',
    "api_key_primary_val":'api_key_primary_val4',
    "request_id":'request_id4'}

    head_dict["LanguagePlay"] = {"host":'host5',
    "api_key":'api_key5',
    "api_key_primary_val":'api_key_primary_val5',
    "request_id":'request_id5'}
    
    body_dict["basic"] = {"host":'host6',
    "api_key":'api_key6',
    "api_key_primary_val":'api_key_primary_val6',
    "request_id":'request_id6'}

    body_dict["review"] = {"host":'host7',
    "api_key":'api_key7',
    "api_key_primary_val":'api_key_primary_val7',
    "request_id":'request_id7'}

    body_dict["CallForAction"] = {"host":'host8',
    "api_key":'api_key8',
    "api_key_primary_val":'api_key_primary_val8',
    "request_id":'request_id8'}
    
    final_dict["head"] = head_dict
    final_dict["body"] = body_dict
    
    return final_dict
        
def make_CompletionExecutor(info_dict, data_type, data_tone):
    completion_executor = CompletionExecutor(
    host=info_dict[data_type][data_tone]["host"],
    api_key=info_dict[data_type][data_tone]["api_key"],
    api_key_primary_val = info_dict[data_type][data_tone]["api_key_primary_val"],
    request_id=info_dict[data_type][data_tone]["request_id"]
    )
    
    return completion_executor
        
def make_request_data():
    request_data = {
        'text': "",
        'maxTokens': 100,
        'temperature': 0.6,
        'topK': 0,
        'topP': 0.8,
        'repeatPenalty': 5.0,
        'start': '',
        'restart': '',
        'stopBefore': ["상품:", "##", "상품 :"],
        'includeTokens': True,
        'includeAiFilters': True,
        'includeProbs': False
    }
    
    return request_data

def make_head_example(test_name, test_key, test_tone):
    if test_tone == "기본":
        example = f"example"
        return example
    
    elif test_tone == "리뷰":
        example = f"example"
        return example
    
    elif test_tone == "행동촉구":
        example = f""
        return example
    
    elif test_tone == "질문":
        example = f"example"
        return example
    
    elif test_tone == "언어유희":
        example = f"example"
        return example


def make_body_example(test_name, test_key, test_tone):
    if test_tone == "기본":
        example = f"example"
        return example
    
    elif test_tone == "리뷰":
        example = f"example"
        return example
    
    elif test_tone == "행동촉구":
        example = f"example"
        return example
    
    
