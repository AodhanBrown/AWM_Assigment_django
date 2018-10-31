from rest_framework import serializers
from .models import Maps

class MapsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maps
        fields = ('id', 'name', 'address', 'location', 'created')
        read_only_fields = ('location',)