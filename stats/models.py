from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.title


class Order(models.Model):
    date = models.DateField()
    products = models.ManyToManyField(Product)
