from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Название группы',
                             max_length=200,
                             help_text='Введите название группы')
    slug = models.SlugField('Слаг',
                            unique=True,
                            help_text='Укажите уникальный адрес для группы')
    description = models.TextField('Описание группы',
                                   help_text='Опишите группу')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Текст поста', help_text='Введите текст поста')
    pub_date = models.DateTimeField('Дата публикации',
                                    auto_now_add=True,
                                    help_text='Дата и время публикации поста')
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Автор',
        help_text='Укажите автора поста'
    )

    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Группа',
        help_text='Укажите группу, к которой относится пост'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:15]
