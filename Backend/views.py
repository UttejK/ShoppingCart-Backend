from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def ProductList(request):  
  # print("testing123", request.accepted_media_type)
  if request.method == 'GET':
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({'products': serializer.data})
  
  if request.method == 'POST':
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def ProductDetail(request):  
  # print("testing123", request.accepted_media_type)
  if request.method == 'GET':
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({'products': serializer.data})
  
  if request.method == 'POST':
    print(request.data)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)