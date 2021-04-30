from rest_framework.views import APIView
import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.settings import api_settings
from django.contrib.auth.models import User

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
        print('53', req)

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
                # json_data = {'errcode':0,'openid':'111','session_key':'test'}
                print('53', json_data)
                if 'errcode' in json_data:
                    return JsonResponse({'status': 500, 'error': '验证错误：' + json_data['errmsg']})
                res = login_or_create_account(json_data)
                print('58', res)
                return JsonResponse(res)
            except:
                return JsonResponse({'status': 500, 'error': '无法与微信验证端连接'})
