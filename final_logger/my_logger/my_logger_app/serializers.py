from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Items , Variant, Property

class UserSerializer(serializers.ModelSerializer):
    username=serializers.CharField( validators = [UniqueValidator(queryset=User.objects.all())])

    def create(self,validated_data):
        user = User.objects.create_user(validated_data['username'])
        return user
    
    class Meta:
        model = User
        fields = ('id','username')

class ItemsSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=100)
    brand=serializers.CharField(max_length=100)
    category=serializers.CharField(max_length=100)
    product_code=serializers.IntegerField()
    class Meta:
        model=Items
        fields=('id','name','brand','category','product_code')

class VariantSerializier(serializers.ModelSerializer):
    item_name=serializers.RelatedField(source='item',read_only=True)
    variant_name=serializers.CharField(max_length=100)
    

    class Meta:
        model=Variant
        fields=('item_name','variant_name','selling_price','cost_price','quantity')

class PropertySerializer(serializers.ModelSerializer):
    item_name=serializers.RelatedField(source='item',read_only=True)
    variant_name=serializers.RelatedField(source='variant',read_only=True)
    attribute_name=serializers.CharField(max_length=100)
    attribute_value=serializers.CharField(max_length=100)
    class Meta:
        model=Property
        fields=('item_name','variant_name','attribute_name','attribute_value')