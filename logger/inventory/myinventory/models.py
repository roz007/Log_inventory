from django.db import models
from myapp.signals import state_audit_signal

class Items(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=90)
    category = models.CharField(max_length=100)
    productcode = models.IntegerField()

    def __str__(self):
        return self.name

class Variant(models.Model):
    name=models.ForeignKey(model=Items,related_name="name")
    selling_prince=models.IntegerField()
    cost_prince=models.IntegerField()
    quantity=models.IntegerField()
    properties=models.ForeignKey(model=Properties,related_name=attribute_name)

    

class Properties(models.Model):
    name=models.ForeignKey(model=Items,related_name="name")
    attribute_name=models.CharField(max_length=100)
    attribute_value=models.CharField(max_length=100)
