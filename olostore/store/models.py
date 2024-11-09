from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    TYPE_CHOICES = [
        ('future', 'Produit à venir'),
        ('available', 'Produit disponible'),
        ('out_of_stock', 'Produit en rupture de stock')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    product_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='available')

    def _str_(self):
        return self.name