from rest_framework import serializers
from stats.models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'price')


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'date', 'products')
