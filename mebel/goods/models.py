from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = "Категорию" 
        verbose_name_plural = "Категории" 

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2,verbose_name="Цена")
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2,verbose_name="Скидка в %")
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(Categories,on_delete=models.CASCADE ,verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = "Продукт" 
        verbose_name_plural = "Продукты"