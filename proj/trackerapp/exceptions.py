'''
Created on Apr 10, 2018

@author: biju
'''
from rest_framework.views import exception_handler   
 
def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
 
    if response is not None:
        response.data = {}
        errors = []
        for field, value in response.data.items():
            errors.append("{} : {}".format(field, " ".join(value)))
 
        response.data['errors'] = errors
        response.data['status'] = False
 
        response.data['exception'] = str(exc)
 
    return response