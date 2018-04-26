'''
Created on Apr 10, 2018

@author: biju
'''
from rest_framework import serializers
from trackerapp.models import UserLocation
from .models import AppUser
class LocationSerializer(serializers.ModelSerializer):
    class Meta:  
        model = UserLocation
        fields = ('id', 'location','latitude','longitude','loctime') 
        many=True       
        
class AppUserSerializer(serializers.ModelSerializer):
    class Meta:  
        model = AppUser
        fields = ('first_name', 'last_name','email','dob') 
        many=True            
    