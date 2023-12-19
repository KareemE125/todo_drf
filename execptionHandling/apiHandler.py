from functools import wraps
from rest_framework.response import Response

from api.models import Todo
from execptionHandling.validationExecption import ValidationException
from execptionHandling.apiError import ApiError

def apiHandler(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except Todo.DoesNotExist as e:
            apiError = ApiError(e, "404 NOT FOUND", f"Todo with ID:'{kwargs.get('pk')}' is not exist")
            return Response(apiError.getJson(), status=404)
            
        except ValidationException as e:
            apiError = ApiError(e, e.statusMessage, "Validation Error", e.description)
            return Response(apiError.getJson(), status=e.statusCode)
            
        except Exception as e:
            apiError = ApiError(e, "500 Internal Server Error")
            return Response(apiError.getJson(), status=500)
    
    return wrapper