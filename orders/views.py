from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Order
from .serializers import OrderSerializer, OrderStatusUpdateSerializer
from django.db.models import Q

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_buyer:
            raise PermissionError("Only buyers can place orders.")
        serializer.save(buyer=self.request.user)

class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        order = self.get_object()

        # Only seller of at least one product in this order can update status
        seller_products = order.items.filter(product__seller=user)
        if not user.is_seller or not seller_products.exists():
            raise PermissionDenied("Only seller of the products can update order status.")

        # Optionally, you can validate allowed status transitions here

        serializer.save()

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_buyer:
            return Order.objects.filter(buyer=user)
        elif user.is_seller:
            return Order.objects.filter(items__product__seller=user).distinct()
        return Order.objects.none()

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
