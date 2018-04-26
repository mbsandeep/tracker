from sphinxql import indexes, fields
from .models import AppUser,UserLocation
from django.conf import settings


class AppUserIndex(indexes.Index):
    first_name = fields.Text(model_attr='first_name')
    last_name = fields.Text(model_attr='last_name')
    email = fields.Text(model_attr='email')
   
    class Meta:
        model = AppUser
        settings.INDEXES['source_params'] = {'sql_field_string': ['first_name', 'last_name', 'email',],}


class UserLocationIndex(indexes.Index):
    location = fields.Text(model_attr='location')
  
    class Meta:
        model = UserLocation
        settings.INDEXES['source_params'] = {'sql_field_string': ['location'], }