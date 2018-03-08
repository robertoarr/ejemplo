from rest_framework import permissions
from rest_framework import viewsets
from users.models import Customer, Office
from users.serializers import CustomerSerializer, Officeserializer
from rest_framework.response import Response
from django.http import HttpResponse


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

        # new_office = Office(city=serializer.validated_data.get('city'),
        #                     state=serializer.validated_data.get('state'),
        #                     address=serializer.validated_data.get('address'),
        #                     postal_code=serializer.validated_data.get('postal_code'))
        # new_office.save()

        serializer.save()
        return Response(serializer.data)
