from rest_framework import serializers
from orders.models import Product, Order

class OrderSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model =
    #     fields = ()
    class Meta:
        model = Order
        fields = ("customer", "order_date", "shipped_date", "comments")

    # customer = serializers.ForeignKey()
    # order_date = serializers.DateTimeField(editable=False)
    # shipped_date = serializers.DateTimeField()
    # status = serializers.CharField(max_length=10)
    # comments = serializers.CharField(max_length=400)    #
    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    # def create(self, validated_data):
    #     order_data = validated_data.pop(' ')
    #     user = User.objects.create(**validated_data)
    #     Order.objects.create(user=user, **customer_data)
    #     return user


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50, required=True)
    description = serializers.CharField(max_length=400)
    price = serializers.IntegerField()
    stock = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    # def validate_name(self, value):
    #     try:
    #         Product.objects.get(name=value)
    #         return value
    #     except:
    #         raise serializers.ValidationError("El producto proporcionado no existe")
