from .models import Article, FileModel, Category, Question, Feedback, Record
from .serializers import ArticleSerializer, FileSerializer, CategorySerializer, QuestionSerializer, FeedbackSerializer, \
    RecordSerializer
from .serializers import ArticleFilter
from app.utils.viewset_base import CustomViewBase
from django_filters import rest_framework
from django.http import JsonResponse
from rest_framework.views import APIView
from app.result_config import *
from django.db.models import Q
from app.login.access import AdministratorLevel


# 文章
class ArticleViewSet(CustomViewBase):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = ['title', 'content']
    permission_classes = (AdministratorLevel,)  # 权限管理

    def perform_create(self, serializer):
        serializer.save()


# 文件
class FileViewSet(CustomViewBase):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer


# 分类
class CategoryViewSet(CustomViewBase):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = ['title', 'type']
    permission_classes = (AdministratorLevel,)  # 权限管理

    def perform_create(self, serializer):
        serializer.save()


# 问题
class QuestionViewSet(CustomViewBase):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = ['title', 'type']
    permission_classes = (AdministratorLevel,)  # 权限管理

    def perform_create(self, serializer):
        serializer.save()


# 反馈
class FeedbackViewSet(CustomViewBase):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = []

    def perform_create(self, serializer):
        serializer.save()


# 结果记录
class RecordViewSet(CustomViewBase):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = []
    permission_classes = (AdministratorLevel,)  # 权限管理

    def perform_create(self, serializer):
        serializer.save()


class RecordDetailView(APIView):

    def get(self, request, pk, format=None):
        record = Record.objects.get(pk=pk)
        mbti = ResultConfig.mbti()
        tags = mbti[record.title]['tag'].split("、")
        print(tags)
        q = Q()
        for tag in tags:
            q |= Q(title__icontains=tag)
        articles = Article.objects.filter(q)
        print(articles)
        serialized = ArticleFilter(articles, many=True).data
        resp = {
            'title': record.title,
            'desc': record.content,
            'articles': serialized
        }

        result = {
            'code': 200,
            'message': 'success',
            'data': resp,
        }
        return JsonResponse(result)
