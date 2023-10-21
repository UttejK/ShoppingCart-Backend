from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Product, Purchase, Cart
from .serializers import ProductSerializer, PurchaseSerializer, CartSerializer


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        productid = self.request.query_params.get('id')
        if productid is not None:
            queryset = queryset.filter(id=productid)
        return queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class PurchaseList(generics.ListCreateAPIView):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer
#
#     def get_queryset(self):
#         queryset = Purchase.objects.all()
#         productid = self.request.query_params.get('id')
#         if productid is not None:
#             queryset = queryset.filter(id=productid)
#         return queryset
#
#
# class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer

class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        queryset = Purchase.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'product'

    def get_queryset(self):
        queryset = Cart.objects.all()
        productid = self.request.query_params.get('id')
        if productid is not None:
            queryset = queryset.filter(id=productid)
        return queryset


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'product'

    def get_object(self):
        product_id = self.kwargs.get('product')
        obj = get_object_or_404(Cart, product=product_id)
        return obj
