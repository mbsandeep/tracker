'''
Created on Apr 10, 2018

@author: biju
'''
from math import radians, sin, cos, acos

def lat_long_distance(lat1,lat2,lon1, lon2):
    try:
        lat1 = radians(lat1)
        lat2 = radians(lat2)
        lon1 = radians(lon1)
        lon2 = radians(lon2)    
        return 6371.01 * acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon1 - lon2))
    except:
            return 0.0       