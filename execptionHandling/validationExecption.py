class ValidationException(Exception):
    statusMessage = "400 BAD REQUEST"   

    def __init__(self, description):
        self.description = description