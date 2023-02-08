from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import LandLordSerializer, LocationSerializer, PropertycategorySerializer, PropertySerializer
from .models import LandLord, Location, Propertycategory, Property

from rest_framework import status

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [

        # landlord
        '/landlords/',
        '/landlord/<id>/',

        # location
        '/locations/',
        '/location/<id>/',

        # property category
        '/property-categories/',
        '/property-category/<id>/',


        # property
        '/properties/',
        '/property/<id>/',

        # Admin
        '/admin/',


    ]
    return Response(routes)

# ==============================================================================================
# landlord


@api_view(['GET', 'POST'])
def getLandLords(request):
    if request.method == 'GET':
        landlords = LandLord.objects.all()
        serializer = LandLordSerializer(landlords, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LandLordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getLandLord(request, pk):
    try:
        landlord = LandLord.objects.get(id=pk)
    except LandLord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LandLordSerializer(landlord, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LandLordSerializer(landlord, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        landlord.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# =================================================================================================
# location


@api_view(['GET', 'POST'])
def getLocations(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getLocation(request, pk):
    try:
        location = Location.objects.get(id=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationSerializer(location, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ==================================================================================================
# property category


@api_view(['GET', 'POST'])
def getProperyCategories(request):
    if request.method == 'GET':
        propertycategories = Propertycategory.objects.all()
        serializer = PropertycategorySerializer(propertycategories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PropertycategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getPropertyCategory(request, pk):
    try:
        propertycategory = Propertycategory.objects.get(id=pk)
    except Propertycategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PropertycategorySerializer(propertycategory, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PropertycategorySerializer(
            propertycategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        propertycategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# =====================================================================================================
# property


@api_view(['GET', 'POST'])
def getProperies(request):
    if request.method == 'GET':
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getProperty(request, pk):
    try:
        property = Property.objects.get(id=pk)

    except Property.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PropertySerializer(property, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
