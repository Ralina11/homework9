from django.urls import path

from main.apps import MainConfig
from main.views import ProductsListView, CategoryListView, OneProductDetailView, ProductCreateView, \
    OneProductUpdateView, OneProductDeleteView

app_name = MainConfig.name



urlpatterns = [
    path('', ProductsListView.as_view(), name='index_list'),
    path('categories/', CategoryListView.as_view(), name='categories_list'),
    path('<int:pk>/product/', OneProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', OneProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', OneProductDeleteView.as_view(), name='product_delete'),

]
