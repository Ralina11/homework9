from django.shortcuts import render

from main.models import Category, Product


# Create your views here.
def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Товары'
    }
    return render(request, 'main/index.html', context)

def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории'
    }
    return render(request, 'main/categories.html', context)