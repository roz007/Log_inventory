from django.db import models
from django.contrib.auth.models import User

class Items(models.Model):
    name=models.CharField(max_length=100)
    Brand=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    Product_code=models.IntegerField()

    def __str__(self):
        return self.name

class Property(models.Model):
    name=models.ForeignKey(Items,on_delete=models.CASCADE)
    Attribute_name=models.CharField(max_length=100)
    Attribute_value=models.CharField(max_length=100)

    def __str__(self):
        return ('%s %s ' % (self.Attribute_name, self.Attribute_value))

class Variant(models.Model):
    name=models.ForeignKey(Items,on_delete=models.CASCADE)
    property_name=models.ForeignKey(Property,on_delete=models.CASCADE)
    selling_price=models.IntegerField()
    cost_price=models.IntegerField()
    quantity=models.IntegerField()

    def __str__(self):
        return ('%s %s ' % (self.name, self.property_name))

