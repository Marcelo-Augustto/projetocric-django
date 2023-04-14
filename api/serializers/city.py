from rest_framework import serializers
from cities.models.city import City
from .route import RouteSerializer

class CitySerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    class Meta:
        model = City
        fields = ('id', 'name', 'banner_photo', 'routes')

class CityDetailSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'routes')