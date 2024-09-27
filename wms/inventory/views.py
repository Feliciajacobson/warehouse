from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializer import OrderSerializer,InventoryMovementSerializer
from .models import Order,InventoryMovement


#CREATE ITEMS
@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_inventory_movement(request):
    serializer = InventoryMovementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE ITEMS
@api_view(['DELETE'])
def delete_inventory_movement(request, pk):
    try:
        inventory_movement = InventoryMovement.objects.get(pk=pk)
    except InventoryMovement.DoesNotExist:
        return Response({'error': 'InventoryMovement not found'},status=status.HTTP_404_NOT_FOUND)
    inventory_movement.delete()
    return Response({'message': 'InventoryMovement deleted successfully'},status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'},status=status.HTTP_404_NOT_FOUND)
    order.delete()
    return Response({'message': 'Order deleted successfully'},status=status.HTTP_204_NO_CONTENT)

#UPDATE ITEMS
@api_view(['PUT'])
def update_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_inventory_movement(request, pk):
    try:
        inventory_movement = InventoryMovement.objects.get(pk=pk)
    except InventoryMovement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = InventoryMovementSerializer(inventory_movement, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET ITEMS
@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_inventory_movements(request):
    inventory_movements = InventoryMovement.objects.all()
    serializer = InventoryMovementSerializer(inventory_movements, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_inventory_movement(request, pk):
    try:
       inventory_movement= InventoryMovement.objects.get(pk=pk)  
    except inventory_movement.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)  
    serializer = InventoryMovementSerializer(inventory_movement)
    return Response(serializer.data)

