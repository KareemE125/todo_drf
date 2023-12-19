class ApiError:
    def __init__(self, error, statusMessage, message=None, description=None):
       self.message = str(message) if message else str(error) 
       self.description = str(description) if description else (str(error.__doc__)  if description else str(error))
       self.statusMessage = statusMessage
       self.errors = list(error.args)
       self.exceptionOrigin = error.__class__.__name__
       
    def getJson(self):
        return {
            "message": self.message, 
            "description": self.description,
            "status": self.statusMessage,
            "errors": self.errors,
            "exception_origin": self.exceptionOrigin,
        }
