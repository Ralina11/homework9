
from django.shortcuts import render

from main.models import Category, Product


# Create your views here.
def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title':'Каталог'
    }
    return render(request, 'main/index.html', context)

def categories(request):
    context = {
        'object_list': Category.object.all(),
        'title':'Полный каталог'
    }
    return render(request, 'main/categories.html', context)

def categories_product(request):
    context = {
        'object_list': Product.object,
        'title':'Полный каталог'
    }
    return render(request, 'main/categories.html', context)