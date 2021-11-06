from .models import Cart
from rest_framework import serializers
from apps.users.serializers import UserSerializer
from apps.products.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'id',
            'product',
            'quantity',
            'total_price'
        ]
        depth = 1

class CartUpdateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Cart
        fields = '__all__'

    def validate(self, data):
        errors = {}
        if 'quantity' not in data or not data['quantity']:
            errors['quantity'] = ['quantity is required.']

        if bool(errors):
            raise serializers.ValidationError(errors)

        return data

        