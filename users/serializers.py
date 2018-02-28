from rest_framework import serializers
from users.models import Customer, Office, Payment
from django.contrib.auth.models import User

from datetime import datetime, timezone

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


class DetailPaymentSerializer(serializers.ModelSerializer):

    expenses = serializers.SerializerMethodField()
    days_from_payment = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ("payment_date", "amount", "expenses", "days_from_payment")

    def get_expenses(self, object):
         IVA = 0.15 * object.amount
         administrative_cost = 0.22* object.amount
         shipping_cost = 0.2 * object.amount
         return {"IVA": IVA, "administrativos": administrative_cost, "embarque": shipping_cost}

    def get_days_from_payment(self, object):
        print (datetime.now(timezone.utc))
        print (object.payment_date)
        return (datetime.now(timezone.utc) - object.payment_date).days
