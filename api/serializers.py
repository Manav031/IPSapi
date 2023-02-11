from rest_framework import serializers
from .models import Building, AccessPoint, Location

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"

class AccessPointSerialzer(serializers.ModelSerializer):
    class Meta:
        model = AccessPoint
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"