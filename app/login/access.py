'''
视图样例：
'''
from django.http import JsonResponse
from rest_framework_jwt.views import APIView
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import permissions
from django.contrib.auth.models import User
import json

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'POST']:
            return True
        return obj.user == request.user


class test_view(APIView):
    http_method_names = ['post']  # 限制api的访问方式
    authentication_classes = (authentication.SessionAuthentication, JSONWebTokenAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)  # 权限管理

    def post(self, request):  # 视图函数
        user = request.user.username
        U = User.objects.get(username=user)
        json_data = json.loads(request.body)
        try:
            test = json_data['']
        except:
            return JsonResponse({'status': 500, 'errmsg': '参数不全'})
        try:
            U.save()
        except:
            return JsonResponse({'status': 500, 'errmsg': '数据库错误'})
        return JsonResponse({'status': 200})
