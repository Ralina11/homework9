from django.db import models


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

    def __str__(self):
        return f'{self.name} ({self.price})'


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты '


