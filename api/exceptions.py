class ValidationError(Exception):
    statusCode = 400
    statusMessage = "400 BAD REQUEST"   

    def __init__(self, description):
        self.description = description
