from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DietaryItemSerializer, OrderSerializer
from .models import DietaryItem, Order


@api_view(['GET'])
def dietary_item_collection(request):
    if request.method == 'GET':
        dietary_items = DietaryItem.objects.all()
        serializer = DietaryItemSerializer(dietary_items, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def dietary(request):
    if request.method == 'GET':
        dietary_items = DietaryItem.objects.all()
        serializer = DietaryItemSerializer(dietary_items, many=True)
        return Response(serializer.data)



