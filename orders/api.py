from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse

from orders.models import Product, Order
from orders.serializers import ProductSerializer, OrderSerializer
#SWAAAAAAAAAGGGGG

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.save())
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)
