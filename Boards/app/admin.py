from django.contrib import admin
from .models import Post, Board

# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('title', 'body', 'author')
@admin.register(Board)
class Board(admin.ModelAdmin):
    list_display = ('title', 'category', 'moderator')
