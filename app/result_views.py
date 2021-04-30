from django.http import JsonResponse
from rest_framework.views import APIView
from collections import Counter
import json
from operator import itemgetter
from .models import Article
from .serializers import ArticleFilter
from django.db.models import Q
from app.result_config import *


class ResultAPI(APIView):
    def post(self, req):
        try:
            answer = req.data['answer']
        except KeyError:
            return JsonResponse({
                'code': 200,
                'message': 'success',
                'data': '参数不正确'
            })
        else:
            mbti = ResultConfig.mbti()
            if not isinstance(answer, list):
                lst = json.loads(answer)
                res = Counter(lst)

            else:
                res = Counter(answer)

            def subdict(d, ks):
                return dict(zip(ks, itemgetter(*ks)(d)))

            def getMax(list=[]):
                dst = subdict(res, list)
                return max(dst, key=dst.get)

            r_list = [getMax(['I', 'E']), getMax(['N', 'S']), getMax(['F', 'T']), getMax(['P', 'J'])]
            r_str = ''.join(r_list)
            print(mbti[r_str]['tag'])
            tags = mbti[r_str]['tag'].split("、")
            q = Q()
            for tag in tags:
                q |= Q(title__icontains = tag)
            articles = Article.objects.filter(q)
            serialized = ArticleFilter(articles, many=True).data
            resp = {
                'val': r_str,
                'desc': mbti[r_str],
                'articles': serialized
            }

            result = {
                'code': 200,
                'message': 'success',
                'data': resp,
            }
            return JsonResponse(result)
