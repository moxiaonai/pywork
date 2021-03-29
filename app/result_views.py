from django.forms import model_to_dict
from django.http import QueryDict, JsonResponse
from app.models import *
from rest_framework.views import APIView

class ResultAPI(APIView):
    def post(self, req):
#         person = [model_to_dict(i) for i in data]
        result = {
            'code': 200,
            'message': 'success',
            'data': req.query_params.dict()
        }
        return JsonResponse(result)