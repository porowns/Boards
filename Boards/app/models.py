from django.db import models
from django.core.urlresolvers import reverse
import uuid
from django.contrib.auth.models import User, Group

# Create your models here.
class Category(models.Model):
    """
    Model representing categories for boards.
    """
    CATEGORY_CHOICES = (
        ('MATH', 'MATH'),
        ('SCIENCE', 'SCIENCE'),
        ('HISTORY', 'HISTORY'),
        ('GENERAL', 'GENERAL'),
    )

    name = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='GENERAL')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('view-category', args=[str(self.id)])

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
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
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
    board = models.ForeignKey('Board', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('view-post', args=[str(self.id)])

class Profile(models.Model):
    """
    Model representing a user profile.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    favorites = models.ManyToManyField('Board')
    friends = models.ManyToManyField(User, related_name='%(class)s_request_friends')
    enemies = models.ManyToManyField(User, related_name='%(class)s_request_enemies')

    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
