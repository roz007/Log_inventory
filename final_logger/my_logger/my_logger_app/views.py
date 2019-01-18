from django.shortcuts import render
from django.contrib.auth import authenticate
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)

from .models import Items , Variant , Property
from .serializers import UserSerializer, ItemsSerializer , VariantSerializier , PropertySerializer


@api_view(['POST'])
@csrf_exempt
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    if username is None:
        return Response(
            {'error':'Please provide username'}
        )
    
    user = authenticate(username=username)
    if not user:
        return Response(
            {'error':'Invalid credentials'},
            status=HTTP_404_NOT_FOUND)
    token, _=Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)

@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors)


@api_view(["POST"])
def register_item(request):
    item_object = ItemsSerializer(
        data={
            'name':request.data['name'],
            'brand':request.data['brand'],
            'category':request.data['category'],
            'product_code':request.data['product_code']
        }
    )
    
    if item_object.is_valid():
        item_object.save()
        return Response(item_object.data,status=HTTP_201_CREATED)
    return Response('item_object.errors') 

@api_view(["POST"])
def register_variant(request):
    try:
        selected_item = Items.objects.get(id=request.data['item_name'])
        serializer=VariantSerializier(
            data={
                'item_name':selected_item,
                'variant_name':request.data['variant_name'],
                'selling_price':request.data['selling_price'],
                'cost_price':request.data['cost_price'],
                'quantity':request.data['quantity']
            }

        )
        if serializer.is_valid():
            print('daivam')
            p =Variant.objects.create(
            item=selected_item,
            variant_name=request.data['variant_name'],
            selling_price=request.data['selling_price'],
            cost_price=request.data['cost_price'],
            quantity=request.data['quantity']
            )
            p.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        
    except Items.DoesNotExist:
        print("meh")
        return Response({'error': 'Item Doesnt Exist'})

@api_view(["POST"]) 
def register_property(request):
    try:
        selected_item= Items.objects.get(id=request.data['item_name'])
        selected_variant=Variant.objects.get(id=request.data['variant_name'])
        property_serializer=PropertySerializer(
                data={
                    'item_name':selected_item,
                    'variant_name':selected_variant,
                    'attribute_name':request.data['attribute_name'],
                    'attribute_value':request.data['attribute_value']
                
                }
        )
        if property_serializer.is_valid():
            print("adi sucka")
            q=Property.objects.create(
                item=selected_item,
                variant=selected_variant,
                attribute_name=request.data['attribute_name'],
                attribute_value=request.data['attribute_value']
            )
            q.save()
            return Response(property_serializer.data,status=HTTP_201_CREATED)
    
    except Items.DoesNotExist or Variant.DoesNotExist:
        print("meg")
        return Response({'error': 'Item/variant Doesnt Exist'})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

   
