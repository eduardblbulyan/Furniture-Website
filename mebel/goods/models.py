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
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2,verbose_name="Скидка в %")
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(Categories,on_delete=models.CASCADE ,verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        db_table = "product"
        verbose_name = "Продукт" 
        verbose_name_plural = "Продукты"

    def display_id(self):
        return f"{self.id:05}" #for example 00025, 00007
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100,2)
        else:
            return self.price


# operator AND
# Product.objects.filter(price__lt=200) & Product.objects.filter(price__gt=50).order_by("price")
# or you can use this
# Product.objects.filter(price__lt=200).filter(price__gt=50).order_by("price")

# DJANGO reads from left to right

# using OR
# Product.objects.filter(price__lt=200) | Product.objects.filter(price__gt=50).order_by("price")



# to get all data from DB in JSON file with these commands (fixture)
# create fixtures/goods in root dir
# cd root dir
# >>> python3 mebel/manage.py dumpdata goods.Categories > fixtures/goods/cats.json
# >>> python3 mebel/manage.py dumpdata goods.Product > fixtures/goods/prods.json

# delete all migrations and db
# create superuser again

# then load all data again
# >>> python3 mebel/manage.py loaddata fixtures/goods/prods.json
# >>> python3 mebel/manage.py loaddata fixtures/goods/cats.json