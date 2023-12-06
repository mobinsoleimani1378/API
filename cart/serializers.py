from rest_framework import serializers

from cart.models import Order, OrderItem
from product.models import Product


class CartSer(serializers.Serializer):
    size = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=100)
    quantity = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    image = serializers.CharField(max_length=100)
    id = serializers.IntegerField()


class OrderSer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='fullname', read_only=True)

    class Meta:
        model = Order
        fields = ('user', 'total_price', 'adress',)


class OrderItemSer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
