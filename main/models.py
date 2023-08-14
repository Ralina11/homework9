from django.db import models
from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
        ordering = ('name',)  # Сортировка по имени


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    picture = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан', **NULLABLE)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='изменен', **NULLABLE)
    price = models.FloatField(verbose_name='цена')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.price})'


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты '

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=350, verbose_name='название версии')

    active_version = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product} - {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


