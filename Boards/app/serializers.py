from rest_framework import serializers
from .models import Post, Board, User

class PostSerializer(serializers.ModelSerializer):
    board = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('title', 'body', 'board', 'author')

class BoardSerializer(serializers.ModelSerializer):
    moderator = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Board
        fields = ('title', 'moderator', 'category')
