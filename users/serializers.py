from rest_framework import serializers
from users.models import Customer, Office
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
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


class Officeserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    city = serializers.CharField(max_length=50, required=True)
    state = serializers.CharField(max_length=50, required=True)
    address = serializers.CharField(max_length=50, required=True)
    postal_code = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Office.objects.create(**validated_data)
