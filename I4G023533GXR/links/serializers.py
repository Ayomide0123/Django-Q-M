from django.urls import path, include
from .models import Link
from rest_framework import routers,  serializers

# Serializers define the API representation.


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
