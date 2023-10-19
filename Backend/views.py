from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer

def ProductList(requset):
  # get all the products
  # serialize them
  # return a json object
  products = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return JsonResponse(serializer.data, safe=False)