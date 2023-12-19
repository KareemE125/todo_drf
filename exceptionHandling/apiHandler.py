from functools import wraps
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed 

from exceptionHandling.validationExecption import ValidationException
from exceptionHandling.apiError import ApiError
from django.core.exceptions import ObjectDoesNotExist
import jwt

def apiHandler(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        
        except KeyError as e:
            apiError = ApiError(e, "400 BAD REQUEST", "Missing Key: " + str(e))
            return Response(apiError.getJson(), status=401)
        
        except (jwt.exceptions.InvalidTokenError, jwt.exceptions.ExpiredSignatureError) as e:
            apiError = ApiError(e, "401 NOT AUTHENTICATED", "Invalid Token")
            return Response(apiError.getJson(), status=401)
    
        except ObjectDoesNotExist as e:
            message = f"Object with ID:'{kwargs.get('pk')}' is not exist" if kwargs.get('pk') else None
            apiError = ApiError(e, "404 NOT FOUND", message)
            return Response(apiError.getJson(), status=404)
            
        except ValidationException as e:
            apiError = ApiError(e, e.statusMessage, "Validation Error", e.description)
            return Response(apiError.getJson(), status=e.statusCode)
        
        except AuthenticationFailed as e:
            apiError = ApiError(e, "400 BAD REQUEST", "Validation Error")
            return Response(apiError.getJson(), status=400)
        
        except Exception as e:
            apiError = ApiError(e, "500 Internal Server Error")
            return Response(apiError.getJson(), status=500)
    
    return wrapper