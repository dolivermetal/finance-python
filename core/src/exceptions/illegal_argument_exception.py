class IllegalArgumentException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.name = 'Illegal Argument'
        self.status_code = 400

    def to_dict(self):
        return {'error': str(self.message)}