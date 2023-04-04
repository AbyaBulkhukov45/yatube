from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

   
class Group(models.Model):
    title = models.CharField('Название группы',max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField('Описание группы')
    
    def __str__(self):
        return self.title

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    ) 
    
    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='posts'
    )