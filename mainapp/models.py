from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('название', max_length=64)
    description = models.TextField('описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        # ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField('название', max_length=64)
    description = models.TextField('описание', blank=True)
    short_desc = models.CharField('краткое описание', max_length=200, blank=True)
    image = models.ImageField(upload_to='product-img', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)

    def __str__(self):
        return f'{self.name} ({self.category_id})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        # ordering = ['name']
