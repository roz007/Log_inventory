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


