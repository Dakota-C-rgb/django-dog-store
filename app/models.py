from django.db import models
from datetime import datetime

# Create your models here.
class DogProduct(models.Model):
    name = models.TextField()
    product_type = models.TextField()
    dog_size = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

class Purchase(models.Model):
    dog_product = models.ForeignKey(DogProduct, on_delete=models.PROTECT)
    purchased_at = models.DateField(datetime.now())

class DogTag(models.Model):
    owner_name = models.TextField()
    dog_name = models.TextField()
    dog_birthday = models.DateField()
    owner_address = models.TextField()
    dog_color = models.TextField()