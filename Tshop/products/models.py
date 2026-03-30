from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 500)
    thumbnail = models.ImageField(upload_to = 'products/thumbnails/')
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'Product : {self.title}'


class ProductImage(models.Model):
    image = models.ImageField(upload_to = 'products/images/')
    caption = models.CharField(max_length = 50)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='image')

    def __str__(self):
        return f'{self.caption} image of > Product {self.product.title}'