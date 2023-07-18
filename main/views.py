from django.shortcuts import render

from main.models import Category, Product


# Create your views here.
def index(request):
    """Контроллер страницы со всеми товарами"""
    context = {
        'object_list': Product.objects.all(),
        'title': 'Товары'
    }
    return render(request, 'main/index.html', context)

def categories(request):
    """Контроллер страницы со списком категорий"""
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории'
    }
    return render(request, 'main/categories.html', context)

def one_product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': f'Продукт {product_item.name}'
    }
    return render(request, 'main/product.html', context)
