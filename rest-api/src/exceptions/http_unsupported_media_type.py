class HttpUnsupportedMediaTypeException(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'Unsupported Media Type'
        self.status_code = 415
