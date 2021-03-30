from django.forms import model_to_dict
from django.http import QueryDict, JsonResponse
from app.models import *
from rest_framework.views import APIView
from collections import Counter
import json
from operator import itemgetter

from app.result_config import *

class ResultAPI(APIView):
    def post(self, req):
        print(ResultConfig.mbti)
        try:
            answer =  req.data['answer']
        except KeyError:


             return JsonResponse({
                 'code': 200,
                 'message': 'success',
                 'data': '参数不正确'
             })
        else:
             mbti = ResultConfig.mbti()
             print(answer)
             lst = json.loads(answer)
             res = Counter(lst)

             def subdict(d, ks):
                 return dict(zip(ks, itemgetter(*ks)(d)))

             def getMax(list):
                 dst = subdict(res, list)
                 return max(dst, key=dst.get)

             print(getMax(['I','E']))
             r_list = [getMax(['I','E']), getMax(['N','S']), getMax(['F','T']), getMax(['P','J'])]
             r_str = ''.join(r_list)
             result = {
                 'val': r_str,
                 'desc': mbti[r_str]
             }
             result = {
                'code': 200,
                'message': 'success',
                'data': result,
            }
             return JsonResponse(result)