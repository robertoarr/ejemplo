from rest_framework import permissions
from rest_framework import viewsets
from users.models import Customer, Office, Payment
from users.serializers import CustomerSerializer, Officeserializer, Paymentserializer
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

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = Paymentserializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):
        #serializer = Paymentserializer(data=request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


    def list(self, request):
        all_payments = Payment.objects.all()
        serializer = Paymentserializer(all_payments, many=True)

        return Response(serializer.data)

