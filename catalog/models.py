from django.db import models


# Create your models here.

class Category(models.Model):
    """Модель для категорий"""
    name = models.CharField(max_length=150, verbose_name='Название категории', unique=True, help_text='Введите название категории')
    description = models.TextField(verbose_name='Описание категории', help_text='Введите описание категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):
    """Модель для продуктов"""
    name = models.CharField(max_length=150, verbose_name='Название продукта', help_text='Введите название продукта')
    description = models.TextField(verbose_name='Описание продукта', null=True, blank=True, help_text='Введите описание продукта')
    image = models.ImageField(upload_to='photos/', verbose_name='Фотография')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField(help_text='Введите цену продукта')
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
