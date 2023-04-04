from django.urls import path

from . import views

# при создании namespace прописываем апп нэйм в урлах прилд
app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
]
