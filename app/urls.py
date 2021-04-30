from django.urls import re_path
from . import views
from app.result_views import *
from app.login.view import *

upload = views.FileViewSet.as_view({
    'post': 'create'
})

article_list = views.ArticleViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

article_detail = views.ArticleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

category_l = views.CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

category_d = views.CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',

})

question_l = views.QuestionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

question_d = views.QuestionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

feedback = views.FeedbackViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

result_d = ResultAPI.as_view()
login_v = LoginView.as_view()
urlpatterns = [
    re_path(r'^articles/$', article_list),
    re_path(r'^articles/(?P<pk>[0-9]+)$', article_detail),
    re_path(r'^category/$', category_l),
    re_path(r'^category/(?P<pk>[0-9]+)$', category_d),
    re_path(r'^question/$', question_l),
    re_path(r'^question/(?P<pk>[0-9]+)$', question_d),
    re_path(r'^feedback/$', feedback),
    re_path(r'^upload/$', upload),
    re_path('^result/', result_d),
    re_path('^login/$', LoginView.as_view()),                                 # 登录
]
