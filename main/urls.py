from django.urls import path

from main.apps import MainConfig
from main.views import ProductsListView, CategoryListView, OneProductDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='index_list'),
    path('categories/', CategoryListView.as_view(), name='categories_list'),
    path('<int:pk>/product/', OneProductDetailView.as_view(), name='product_detail'),
 ]
