from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogDeleteView, BlogUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),  # создание поста в blogpost_form
    path('', BlogListView.as_view(), name='list'),  # список постов в blogpost_list
    path('view/<int:pk>', BlogDetailView.as_view(), name='view'),  # детали одного поста в blogpost_detail
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit'),  # редактирование поста
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),  # подтверждение и удаление
]