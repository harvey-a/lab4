from rest_framework import serializers
from shop.models import User, Product, Cart

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    date = serializers.DateTimeField()
    ship_address = serializers.CharField(max_length=255)
    id = serializers.IntegerField(read_only=True)
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.ship_address = validated_data.get('ship_address', instance.ship_address)
        instance.save()
        return instance

class ProductSerializer(serializers.Serializer):
    total_price = serializers.FloatField()
    name = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length = 200)
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.name = validated_data.get('name', instance.name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

class CartSerializer(serializers.Serializer):
    cart_code = serializers.DecimalField(decimal_places=3, max_digits=10)
    total_price = serializers.FloatField()
    product = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    paid = serializers.BooleanField()
    id = serializers.IntegerField(read_only=True)
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Cart.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.cart_code = validated_data.get('cart_code', instance.cart_code)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.product = validated_data.get('product', instance.product)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.paid = validated_data.get('paid', instance.paid)        
        instance.save()
        return instance