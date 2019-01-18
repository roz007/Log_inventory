from rest_framework import serializers
from .models import Items , Variant, Property

class ItemsSerializer(serializers.ModelSerialzier):
    name=serializers.CharField(max_length=100)
    brand=serializers.CharField(max_length=100)
    category=serializers.CharField(max_length=100)
    product_code=serializers.IntegerField()
    class Meta:
        model=Items
        fields=('id','name','category','product_code')

class VariantSerializier(serializers.ModelSerialzier):
    item_name=serializers.RelatedField(source='item',read_only=True)
    variant_name=serializers.CharField(max_length=100)
    

    class Meta:
        model=Variant
        fields=('item_name','variant_name','selling_price','cost_price','quantity')

class PropertySerializer(serializers.ModelSerialzier):
    item_name=serializers.RelatedField(source='item',read_only=True)
    variant_name=serializers.RelatedField(source='variant',read_only=True)
    attribute_name=serializers.CharField(max_length=100)
    attribute_value=serializers.CharField(max_length=100)
    class Meta:
        model=Property
        fields=('item_name','variant_name','attribute_name','attribute_value')