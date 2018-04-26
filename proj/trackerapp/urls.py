from django.urls import re_path,path
from .views import UserLocationCRUDView
from .views import UserLocationListCreateView
from .views import UserLocationListView
from .views import UserRouteListView 
from .views import SearchListView 
from .views import SearchUserView
from .views import SearchLocationView
urlpatterns = [    
  
    re_path(r'^locations/(?P<pk>\d+)$', UserLocationCRUDView.as_view(), name='user_locations'),
    re_path(r'^users/(?P<user>\d+)/locations/',UserLocationListView.as_view(), name='locations_for_user'),
    re_path(r'^locations/', UserLocationListCreateView.as_view(), name='user_location_list'),
    re_path(r'^users/(?P<user>\d+)/routes/',UserRouteListView.as_view(), name='routes_for_user'), 
    re_path(r'^search/',SearchListView.as_view(),name='search_view'),
    path('user/search',SearchUserView.as_view(),name='user_search_view'),
    path('location/search',SearchLocationView.as_view(),name='location_search_view')         
]
