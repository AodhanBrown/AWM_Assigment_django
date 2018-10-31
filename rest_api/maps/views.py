from django.shortcuts import render
from rest_framework import viewsets
from .models import Maps
from .serializers import MapsSerializer
from django.contrib.gis.geos import GEOSGeometry
#from rest_framework import status
#from rest_framework import Response
from django.shortcuts import get_object_or_404
from geopy.geocoders import Nominatim

# Create your views here.

# list all the locations oe create a new one 
class MapsView(viewsets.ModelViewSet):
    queryset = Maps.objects.all()
    serializer_class = MapsSerializer

    def perform_create(self, serializer):
        address = serializer.initial_data['address']
        #g = geocoder.google(address)
        geolocator = Nominatim(user_agent="http://127.0.0.1:8000/maps/")
        g = geolocator.geocode(address)
        latitude = g.latitude
        longitude = g.longitude
        pnt = 'POINT(' + str(longitude) + ' ' + str(latitude) + ')'
        serializer.save(location=pnt)
    '''
    def get(self, request):
        return Response(serializer_class.data)

    def post(self, request):
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
            '''

    
