from rest_framework import serializers
from .models import Product, Purchase, Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        # fields = '__all__'
        fields = ('id', 'product', 'user_id', 'quantity', 'amount_paid')

    #
    # def get_product_id(self, obj):
    #     product = obj.product
    #     return product.id


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    #
    # def get_product_id(self, obj):
    #     product = obj.product
    #     return product.id
