from django.db import models


# Create your models here.
class DietaryItem(models.Model):
    # Define Dietary items
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=20)
    shelf_life = models.CharField(max_length=30)
    category = models.CharField(max_length=40)


class Order(models.Model):
    # Define an order
    dietary_item = models.ForeignKey(DietaryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    department = models.CharField(max_length=40)
    facility = models.CharField(max_length=40)

