from rest_framework import permissions
from rest_framework import viewsets
from users.models import Customer, Office
from users.serializers import CustomerSerializer, Officeserializer
from rest_framework.response import Response


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (permissions.AllowAny, )


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = Officeserializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("Hola")
        serializer.save()
        return Response(serializer.data)
