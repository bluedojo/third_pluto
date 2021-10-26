from rest_framework import serializers

from .models import *


class DietaryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryItem
        fields = ['id', 'title', 'cost', 'unit', 'shelf_life', 'category']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'dietary_item', 'quantity', 'department', 'facility']

