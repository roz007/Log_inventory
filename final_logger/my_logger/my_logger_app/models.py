from django.db import models
from django.contrib.auth.models import User

class Items(models.Model):
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    product_code=models.IntegerField()

    def __str__(self):
        return self.name

class Variant(models.Model):
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    variant_name=models.CharField(max_length=100)
    selling_price=models.IntegerField()
    cost_price=models.IntegerField()
    quantity=models.IntegerField()

    def __str__(self):
        return ('%s %s ' % (self.item, self.variant_name))

class Property(models.Model):
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    variant=models.ForeignKey(Variant,on_delete=models.CASCADE)
    attribute_name=models.CharField(max_length=100)
    attribute_value=models.CharField(max_length=100)

    def __str__(self):
        return ('%s %s ' % (self.attribute_name, self.attribute_value))