from django.shortcuts import render, get_object_or_404
from .models import Post, Group


POSTS_PAGES = 10


def index(request):
    template = 'posts/index.html'
    title = 'YA Главная страница'
    posts = Post.objects.order_by('-pub_date')[:POSTS_PAGES]
    context = {
        'posts': posts,
        'title': title,
        'text': 'Это главная страница Yatube',
    }
    return render(request, template, context, {})


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = ' YA Посты'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:POSTS_PAGES]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context, {})
