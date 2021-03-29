from .models import Article, FileModel, Category, Question, Feedback
from .serializers import ArticleSerializer, FileSerializer, CategorySerializer, QuestionSerializer, FeedbackSerializer
from app.utils.viewset_base import CustomViewBase
from django_filters import rest_framework

# 文章
class ArticleViewSet(CustomViewBase):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = ['title', 'content']

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

    def perform_create(self, serializer):
        serializer.save()

# 问题
class QuestionViewSet(CustomViewBase):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = ['title', 'type']

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