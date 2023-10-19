from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render
# from rest_frameworks.decorators import api_view
# 
# @api_view('GET', 'POST')
def ProductList(request):
  products = Product.objects.all()
  print(f"products: {products}")
  serializer = ProductSerializer(products, many=True)
  return JsonResponse({'products': serializer.data})
  # return render(request)pgAdmin 4 started