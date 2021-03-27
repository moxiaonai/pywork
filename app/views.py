from .models import Article, FileModel, Category, Question
from .serializers import ArticleSerializer, FileSerializer, CategorySerializer, QuestionSerializer
from app.utils.viewset_base import CustomViewBase

# 文章
class ArticleViewSet(CustomViewBase):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

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

    def perform_create(self, serializer):
        serializer.save()

# 问题
class QuestionViewSet(CustomViewBase):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save()