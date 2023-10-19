from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ("id","name","total_available","price","image_url","description","category")
    