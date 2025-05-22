from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'buyer', 'order_date', 'status', 'items']
        read_only_fields = ['buyer', 'order_date']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        buyer = self.context['request'].user  # or remove this line entirely
        order = Order.objects.create(**validated_data)  # don't pass buyer again
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
    
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Order.STATUS_CHOICES)

    class Meta:
        model = Order
        fields = ['status']
