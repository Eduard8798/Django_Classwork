from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from rest_framework import status

#create car
@api_view(['POST'])
def create_car(request):
    print("__data",request.data)
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_single_car(request,pk):
    car = Car.objects.get(pk=pk)
    serializer = CarSerializer(car)
    return Response(serializer.data)

@api_view(['PUT'])
def update_car(request,pk):
    car = Car.objects.get(pk=pk)
    serializer = CarSerializer(car, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_car(request,pk):
    car = Car.objects.get(pk=pk)
    car.delete()
    return Response( status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)
