from rest_framework import serializers
from .models import Post, Board, User

class PostSerializer(serializers.Serializer):
    """
    List all posts, or create one.
    """
    title = serializers.CharField(required=True, max_length=20)
    body = serializers.CharField(required=True, max_length=300)
    #author = serializers.ChoiceField(required=True, choices=User.objects.all())

    def create(self, validated_data):
        """
        Create and return a Post instance.
        """
        return Post.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.author = validated_data.get('author', instance.author)
