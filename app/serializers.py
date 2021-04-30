from rest_framework import serializers
from .models import Article, FileModel, Category, Question, Feedback, Record

class ArticleSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'create_date')

class ArticleFilter(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Article
        fields = ['id','title','create_date','content']
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

class RecordSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ('id', 'create_date')
        depth = 1