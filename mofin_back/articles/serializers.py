from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer

class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users', 'nickname')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article', 'like_users', 'nickname')

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.ReadOnlyField(source='user.username')
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users', 'nickname')

    def get_is_liked(self, obj):
        request = self.context.get('request')
        return request and request.user.is_authenticated and request.user in obj.like_users.all()