from django.contrib import admin
from .models import Post, Board, Category, Profile

# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('title', 'body', 'author')

@admin.register(Board)
class Board(admin.ModelAdmin):
    list_display = ('title', 'category', 'moderator')

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name', 'id')

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('id', 'id')
