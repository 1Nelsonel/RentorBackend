from rest_framework import serializers
from .models import LandLord,Location,Propertycategory,Property


class LandLordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandLord
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class PropertycategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Propertycategory
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'