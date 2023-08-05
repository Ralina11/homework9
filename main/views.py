from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import ProductForm
from main.models import Category, Product


# Create your views here.

class ProductsListView(ListView):
    """Контроллер страницы со всеми товарами"""
    model = Product
    template_name = 'main/index_list.html'
    context_object_name = 'object_list'
    extra_context = {
        'title': 'Товары'
    }
def index(request):
    """Контроллер страницы со всеми товарами"""
    context = {
        'object_list': Product.objects.all(),
        'title': 'Товары'
    }
    return render(request, 'main/index_list.html', context)

def categories(request):
    """Контроллер страницы со списком категорий"""
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории'
    }
    return render(request, 'main/categories_list.html', context)

class CategoryListView(ListView):
    """Контроллер страницы со списком категорий"""
    model = Category
    template_name = 'main/categories_list.html'
    context_object_name = 'categories_list'
    extra_context = {
        'title': 'Категории товаров'
    }



# def one_product(request, pk):
#     """Контроллер страницы с одним товаром"""
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#         'title': f'Продукт {product_item.name}'
#     }
#     return render(request, 'main/product_detail.html', context)

class OneProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'object'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Product.objects.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['product_pk'] = product_item.pk,
        context_data['title'] = f'  {product_item.name}'

        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("main:index_list")


class OneProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("main:index_list")


class OneProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("main:index_list")