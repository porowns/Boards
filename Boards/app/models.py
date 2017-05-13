from django.db import models
from django.core.urlresolvers import reverse
import uuid
from django.contrib.auth.models import User, Group

# Create your models here.
class Board(models.Model):
    """
    Model representing a board, which will contain posts.
    """

    CATEGORY_CHOICES = (
        ('MATH', 'MATH'),
        ('SCIENCE', 'SCIENCE'),
        ('HISTORY', 'HISTORY'),
        ('GENERAL', 'GENERAL'),
    )

    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='GENERAL')
    moderator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('view-board', args=[str(self.id)])

class Post(models.Model):
    """
    Model representing a post, which will be assigned to a board.
    """
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=2000)
    likes = models.IntegerField
    board = models.ForeignKey('Board', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('view-post', args=[str(self.id)])
