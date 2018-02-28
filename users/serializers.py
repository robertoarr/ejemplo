from rest_framework import serializers
from users.models import Customer, Office, Payment, Employee
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):

#     # user_id = serializers.IntegerField()
#     # dob = serializers.DateField()
#     # phone_number = serializers.CharField(max_length=15)
#     #postal_code = serializers.IntegerFiel(required=True)


    # user_id = serializers.IntegerField()
    # dob = serializers.DateField()
    # phone_number = serializers.CharField(max_length=15)
    #postal_code = serializers.IntegerFiel(required=True)

    class Meta:
        model = Customer
        fields = ("user", "dob", "phone_number", "postal_code")

    def create(self, validated_data):
        customer_data = validated_data.pop(' ')
        user = User.objects.create(**validated_data)
        Customer.objects.create(user=user, **customer_data)
        return user

    # def validate_user(self, value):
    #     try:
    #         Customer.objects.get(user=value)
    #         return value
    #     except:
    #         raise serializers.ValidationError("El usuario proporcionado no existe")


class Officeserializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # city = serializers.CharField(max_length=50, required=True)
    # state = serializers.CharField(max_length=50, required=True)
    # address = serializers.CharField(max_length=50, required=True)
    # postal_code = serializers.IntegerField(required=True)

    class Meta:
        model = Office
        fields = ('id', 'city', 'state', 'address', 'postal_code')
        extra_kwargs = {
            'city': {
                'required': True
            },
            'state': {
                'required': True
            },
            'address': {
                'required': True
            },
            'postal_code': {
                'required': True
            },
            'id': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        return Office.objects.create(**validated_data)

class Paymentserializer(serializers.Serializer):
    # customer = serializers.CharField(source='customer.user.username', read_only=True)
    customer_id = serializers.IntegerField(write_only=True, required=True)
    payment_date = serializers.DateTimeField(read_only=True)
    amount = serializers.IntegerField(required=True)
    hello = serializers.CharField(required=False)

    def validate_customer_id(self, value):
        try:
            Customer.objects.get(pk=value)
            return value
        except:
            raise serializers.ValidationError("El comprador no existe")

    def create(self, validated_data):
        customer = Customer.objects.get(pk=validated_data.get("customer_id"))
        payment = Payment.objects.create(customer=customer, amount=validated_data.get(amount))
        print(validated_data)

        return payment


class EmployeeSerializer(serializers.ModelSerializer):
    username = CharField(required=True)
    email = EmailField(required=True)
    password = CharField(required=True)

    class Meta:
        model = Employee
        fields = ('Employee_id', 'office', 'reports_to', 'extension', 'job_title')
         extra_kwargs = {
            'Employee_id': {
                'read_only': True
             }
        }

        def create(self, validated_data):
            user_employee = User.objects.create(username=username, email=email, password=password)
            employee = Employee.objects.create(**validated_data)
