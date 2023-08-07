from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import ProductForm, VersionForm
from main.models import Category, Product, Version


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data


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

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OneProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("main:index_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        return super().form_valid(form)


class OneProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("main:index_list")

