from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

upload = views.FileViewSet.as_view({
    'post': 'create'
})

article_list = views.ArticleViewSet.as_view({
    'get': 'list',
    'post': 'create'
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
    'delete': 'destroy'
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

urlpatterns = [
    re_path(r'^articles/$', article_list),
    re_path(r'^articles/(?P<pk>[0-9]+)$', article_detail),
    re_path(r'^category/$', category_l),
    re_path(r'^category/(?P<pk>[0-9]+)$', category_d),
    re_path(r'^question/$', question_l),
    re_path(r'^question/(?P<pk>[0-9]+)$', question_d),
    re_path(r'^upload/$', upload),
]

urlpatterns = format_suffix_patterns(urlpatterns)