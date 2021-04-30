from rest_framework import serializers
from .models import Article, FileModel, Category, Question, Feedback


class ArticleSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'create_date')


class CategorySerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id', 'create_date')


class QuestionSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('id', 'create_date')


class FeedbackSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'
        read_only_fields = ('id', 'create_date')


class FileSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = FileModel
        fields = '__all__'
