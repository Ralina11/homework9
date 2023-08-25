from django.urls import path

from main.apps import MainConfig
from main.views import index, categories

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories')
 ]
