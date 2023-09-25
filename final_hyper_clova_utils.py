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
        example = f"##\n상품:현대자동차\n키워드:안전,가족\n메시지:당신 곁엔 언제나 든든한 차가 있습니다. 매일매일 사랑하는 사람들을 지켜줄 수 있도록 더 튼튼하게 만들어졌습니다.\n##\n상품:멀티비타민\n키워드:에너지\n메시지:멀티비타민으로 피로를 날려버리고 에너지 충전! 멀티비타민은 건강한 라이프스타일을 위한 필수 아이템입니다.\n##\n상품:다짐 필라테스\n키워드:무료 레슨 체험\n메시지:건강한 변화를 위한 첫 걸음, 다짐 필라테스의 무료 레슨 체험은 당신의 몸을 더욱 아름답게 가꿀 수 있는 출발점입니다.\n##\n상품:인터파크 동남아투어 패키지\n키워드:특별 혜택 3종 세트\n메시지:인터파크 동남아투어 패키지로 떠나는 설렘 가득한 여행, 특별 혜택 3종 세트로 더욱 특별해 집니다.\n##\n상품:{test_name}\n키워드:{test_key}\n메시지:"
        return example
    
    elif test_tone == "리뷰":
        example = f"##\n상품:현대자동차\n키워드:안전,가족\n메시지:현대자동차의 안전한 운전 환경과 가족 중심의 디자인은 정말 감명 깊어요. 가족 모두가 함께하는 여정을 안심하며 즐길 수 있어서 좋아요.\n##\n상품:멀티비타민\n키워드:에너지\n메시지:원래 건강기능식품 같은 거 잘 안 챙겨 먹는데 이건 꼭 먹어요. 야근과 회식 잦은 직장인들에게 필수템! 확실히 체력적으로 힘든게 덜 하네요.\n##\n상품:다짐 필라테스\n키워드:휴식\n메시지:무료 체험을 통해 다짐 필라테스의 매력을 느낄 수 있어요. 전문 강사와 함께 몸과 마음의 균형을 찾아낼 수 있어요.\n##\n상품:인터파크 동남아투어 패키지\n키워드:특별 혜택 3종 세트\n메시지:특별 혜택 3종 세트로 더욱 특별한 인터파크 동남아투어 패키지! 여행을 더욱 풍성하게 만들어준 최고의 선택이에요.\n##\n상품:{test_name}\n키워드:{test_key}\n메시지:"
        return example
    
    elif test_tone == "행동촉구":
        example = f"##\n상품:현대자동차\n키워드:안전,가족\n메시지:현대자동차로 안전한 카 라이프를 즐기며 가족과 함께하는 특별한 시간을 만들어보세요!\n##\n상품:멀티비타민\n키워드:에너지\n메시지:마이카인드 유기농 멀티비타민을 40% 할인된 가격으로 만나보실 수 있는 절호의 기회! 지금 바로 구입하세요!\n##\n상품:다짐 필라테스\n키워드:무료 레슨 체험\n메시지:날씬한 몸매를 원한다면 지금 바로, 다짐 필라테스에서 무료 1:1 레슨 체험을 예약하세요!\n##\n상품:인터파크 동남아투어 패키지\n키워드:특별 혜택 3종 세트\n메시지:내일까지 인터파크 동남아투어 패키지를 예약하는 분에 한해서 특별 혜택 3종 세트를 드립니다. 지금 바로 예약하세요!\n##\n상품:{test_name}\n키워드:{test_key}\n메시지:"
        return example
    
    elif test_tone == "질문":
        example = f"##\n상품:현대자동차\n키워드:안전,가족\n메시지:가족의 안전과 미래를 보장하는 현대자동차. 현대자동차와 함께하면 어떤 가족의 미래를 그려볼 수 있을까요?\n##\n상품:멀티비타민\n키워드:에너지\n메시지:지긋지긋한 피로! 멀티비타민으로 달라진 하루! 어떤 하루일지 궁금하지 않으세요?\n##\n상품:다짐 필라테스\n키워드:무료 레슨 체험\n메시지:무료 레슨 체험으로 다짐 필라테스의 매력을 직접 확인해 보실래요?\n##\n상품:인터파크 동남아투어 패키지\n키워드:특별 혜택 3종 세트\n메시지:특별 혜택 3종 세트가 더해진 인터파크 동남아투어 패키지, 당신은 이번 기회를 통해 어떤 특별한 순간을 기대하시나요?\n##\n상품:{test_name}\n키워드:{test_key}\n메시지:"
        return example
    
    elif test_tone == "언어유희":
        example = f"##\n상품:현대자동차\n키워드:안전,가족\n메시지:현대(現代)는 늘 새롭게 변화한다. 현대(現代)는 늘 사람을 생각한다. 차 좀 아는 사람들의 현대차\n##\n상품:멀티비타민\n키워드:에너지\n메시지:비타민이 없어도 힘을 낼 수는 있지만, 멀티비타민이 있으면 에너지가 폭발해요.\n##\n상품:다짐 필라테스\n키워드:무료 레슨 체험\n메시지:무료 레슨 체험하러 다짐 필라테스로 Go Go! 다짐 필라테스와 함께하니 피곤함은 어느새 어디로?\n##\n상품:인터파크 동남아투어 패키지\n키워드:특별 혜택 3종 세트\n메시지:특별 혜택 3종 세트로 더욱 특별해진 인터파크 동남아투어 패키지, \"집에 돌아가고 싶지 않은 휴가\" 완성!\n##\n상품:{test_name}\n키워드:{test_key}\n메시지:"
        return example


def make_body_example(test_name, test_key, test_tone):
    if test_tone == "기본":
        example = f"##\n상품:썬크림\n키워드:촉촉\n메시지:새로운 피부 관리 습관을 만들어보세요! 피부 톤을 밝게 만들어주고 동시에 촉촉함을 더해주는 톤업 썬크림으로 자신만의 매력을 뽐내보세요. 썬크림의 톤업 효과는 자연스럽게 피부를 교정하고, 촉촉함은 지친 피부를 화사하게 빛나는 피부로 되살아 나게 하여 주변의 시선을 사로잡는 답니다.\n##\n상품:현대자동차\n키워드:안전,가족\n메시지:안전한 드라이빙으로 가족을 지켜주세요. 현대자동차는 가족의 소중함을 알고 있습니다. 현대자동차의 선진적인 안전 기술과 첨단 시스템은 길 위에서의 모든 여정을 더욱 안전하고 신뢰성 있게 만들어줍니다. 우리는 운전자와 승객의 안전을 위해 끊임없이 연구하며 혁신하고 있습니다. 가족과 함께하는 모든 순간을 더욱 특별하게 만들어줄 현대자동차와 함께하세요.\n##\n상품:MZ청바지\n키워드:트렌디함\n메시지:지금 MZ청바지로 트렌디함을 업그레이드하세요! 젊고 모던한 스타일을 완성하는 비결은 바로 MZ청바지입니다. 더 이상 보통의 청바지로 만족하지 마세요. MZ청바지는 특별한 디자인과 섬세한 디테일로 트렌디한 분위기를 한층 업그레이드시켜줍니다. 모든 룩에 완벽하게 어울리며 스타일을 더욱 돋보이게 해줄 MZ청바지로 자신만의 유니크한 패션을 표현해보세요.\n##\n상품:멀티비타민\n키워드:에너지\n메시지:에너지부터 건강까지, 멀티비타민이 모두 챙겨줍니다! 멀티비타민은 비타민과 미네랄의 조합으로 하루의 에너지를 보충하고, 영양소 공급을 도와줄 뿐만 아니라, 여러분의 체력과 면역을 강화시켜 활기찬 일상을 만들어줍니다. 지친 일상에서 멀티비타민이 함께하면, 피로와 스트레스에 대항하는 더 건강한 나를 발견할 수 있습니다.\n##\n상품:{test_name}\n키워드:{test_key}\n메시지:"
        return example
    
    elif test_tone == "리뷰":
        example = f"##\n상품:톤업 썬크림\n키워드:촉촉\n메시지:톤업 썬크림을 사용하고서 피부 상태가 매일 좋아졌어요. 피부 톤이 밝아지면서 피부가 더욱 생기 있는 느낌이 들고, 촉촉함은 하루 종일 지속돼요. 뭔가 부드럽게 발리면서도 피부에 묻지 않고 자연스럽게 흡수되는 느낌이 좋아요. 햇빛을 가려주는 기능까지 갖춰져 있어서 외출 시에도 편하게 사용할 수 있어서 더 좋아요!\n##\n상품:현대자동차\n키워드:안전, 가족\n메시지:현대자동차의 안전성은 진정한 보물입니다. 가족을 위해 운전하는데 있어서 어떤 것보다 중요한 것은 바로 안전입니다. 그래서 현대자동차를 선택한 것이었죠. 가장 최신 기술로 보호되는 이 자동차는 운전자와 승객의 안전을 위한 완벽한 선택이었습니다. 특히 길 위에서의 안정성과 신뢰성은 절대 어딘가에 뒤떨어지지 않는 것 같아요. 가족과 함께하는 모든 여정이 더욱 평안하고 안전한 이유는 바로 현대자동차 때문입니다.\n##\n상품:MZ청바지\n키워드:트렌디함\n메시지:MZ청바지는 정말 트렌디함을 살린 최고의 선택이에요. 여기서 트렌디함은 단순한 스타일을 넘어서 독특한 매력을 지칭하는데요. 이 청바지는 유행을 주도하는 패션 트렌드를 완벽하게 반영하면서도 개성적인 느낌을 줘요. 고급스러운 디자인과 편안한 착용감이 조화를 이루어 여러분의 스타일에 환상적인 변화를 불러옵니다. MZ청바지로 당신만의 독특한 패션 센스를 표현하며, 어디서든 눈에 띄는 멋을 자랑해보세요.\n##\n상품:멀티비타민\n키워드:에너지\n메시지:멀티비타민은 제가 찾던 답이었습니다. 에너지 부족과 피로로 고민하던 와중에 이 제품을 만났는데, 그 효과가 믿을 수 없을 만큼 크네요. 비타민과 미네랄의 조화가 몸에 깊숙히 스며들어서, 하루 중 힘들고 지친 순간을 훨씬 더 쉽게 이겨낼 수 있게 해줍니다. 멀티비타민 덕분에 내 면모를 더욱 빛나게 발견할 수 있었고, 일상 속에 새로운 활력을 불어넣을 수 있었습니다.\n##\n상품:{test_name}\n키워드:{test_key}\n메시지:"
        return example
    
    elif test_tone == "행동촉구":
        example = f"##\n상품:톤업 썬크림\n키워드:촉촉\n메시지:촉촉한 피부로 더 자신감 있게 빛나보세요! 톤업 썬크림으로 피부에 활력을 불어넣어보세요. 매일 아침, 이 작은 썬크림 한 번 발라보는 건 어떨까요? 햇빛으로부터 피부를 지키고 동시에 촉촉한 상태를 유지하며, 자연스럽게 피부 톤을 높여보세요. 아무런 노력 없이도 더욱 환하고 건강한 피부를 만날 수 있을 거예요. 지금 바로 시작해보세요!\n##\n상품:현대자동차\n키워드:안전, 가족\n메시지:가족을 지키는 선택, 현대자동차와 함께하세요. 도로 위에서의 안전은 우리의 최우선 과제입니다. 현대의 최신 안전 기술과 품질로 가득한 차량들은 당신의 소중한 가족을 위한 완벽한 파트너가 될 것입니다. 가족과 함께하는 모든 순간을 더욱 안전하게 만들어보세요.\n##\n상품:MZ청바지\n키워드:트렌디함\n메시지:트렌디함을 입다, MZ청바지로 스타일을 새롭게 시작해보세요! 내게 딱 맞는 핏과 편안한 착용감으로, 자신감 넘치는 일상을 만들어보세요. MZ청바지와 함께라면 어디든 자유롭게 떠날 수 있는 기분이 들어, 새로운 경험을 위한 떠남을 도와줄 거예요. 지금 당장 MZ청바지로 트렌디한 모습을 완성하고, 세상에 자신만의 스타일을 펼쳐보세요!\n##\n상품:멀티비타민\n키워드:에너지,40% 할인\n메시지:바쁜 일상 속 건강 챙기기 힘드시죠? 건강을 위해 이것저것 챙겨먹자니 귀찮고...이것 하나면 충분해요! 필요한 8가지 비타민을 1알에 담았다! 현대사회 직장인들에게 딱 맞는 멀티비타민이 무려 40%나 할인한다고? 지금 구매하고 추가 증정품 받아가세요!\n##\n상품:{test_name}\n키워드:{test_key}\n메시지:"
        return example
    
    
