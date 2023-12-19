import jwt, datetime
from django.conf import settings

class JWTHelper:
    
    @staticmethod
    def encode(payload):
        payload = {
            **payload, 
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            "iat": datetime.datetime.utcnow()
        }
        return jwt.encode(payload, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
    
    @staticmethod
    def decode(token):
        return jwt.decode(token, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
    
    
    
    
    
    
    
    