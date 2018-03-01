from rest_framework import permissions
from rest_framework import viewsets
from users.models import Customer, Office, Payment, Employee
from users.serializers import CustomerSerializer, Officeserializer, Paymentserializer, EmployeeSerializer
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


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = Paymentserializer
    permission_classes = (permissions.AllowAny, )
    # serializer.save()
    # return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # serializer = Paymentserializer(data=request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def list(self, request):
        all_payments = Payment.objects.all()
        serializer = Paymentserializer(all_payments, many=True)

        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.save()

        return Response(serializer.data)

    def list(self, request):
        all_employees = Employee.objects.all()
        serializer = EmployeeSerializer(all_employees, many=True)

        return Response(serializer.data)



class DetailPaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = Paymentserializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = DetailPaymentSerializer(data=request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def list(self, request):
        all_payments = Payment.objects.all()
        serializer = DetailPaymentSerializer(all_payments, many=True)

        return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data)
