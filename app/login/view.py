from rest_framework.views import APIView
import requests
from django.conf import settings
from django.http import JsonResponse
from app.serializers import *
from django.contrib.auth import login, authenticate

'''
登录函数：
'''

def get_user_info_func(user_code):
    api_url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code'
    get_url = api_url.format(settings.WECHAT['APP_ID'], settings.WECHAT['APP_SECRET'], user_code)
    r = requests.get(get_url)
    return r.json()


def login_or_create_account(json_data):
    openid = json_data['openid']
    session_key = json_data['session_key']
    try:
        user = User.objects.get(username=openid)
        print('user', user)
    except:
        user = User.objects.create(
            username=openid,
            password=openid,
        )
    user.session_key = session_key
    user.save()
    res = {
        'status': 200,
        'openid': openid,
        'session_key': session_key
    }
    return res


class LoginView(APIView):
    def post(self, req):
        try:
            code = req.data['code']
        except KeyError:
            return JsonResponse({
                'code': 200,
                'message': 'success',
                'data': '参数不正确'
            })
        else:
            try:
                json_data = get_user_info_func(code)
                if 'errcode' in json_data:
                    return JsonResponse({'status': 500, 'error': '验证错误：' + json_data['errmsg']})
                res = login_or_create_account(json_data)
                return JsonResponse(res)
            except:
                return JsonResponse({'status': 500, 'error': '无法与微信验证端连接'})


class OpLoginView(APIView):
    queryset = User.objects.all()
    serializer_class = LogSerializers

    def post(self, request, *args, **kwargs):
        data = request.data
        res = LogSerializers(data=data)

        if res.is_valid():
            username = request.data['username']
            password = request.data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)  # 校验完正确性之后登录
            request.session['is_login'] = True
            response = JsonResponse({
                'code': 200,
                'message': 'success',
                'data': '登录成功'
            })
            return response

        return JsonResponse({
            'code': 200,
            'error': '账号或者密码错误',
        })
