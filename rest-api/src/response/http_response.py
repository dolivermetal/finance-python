# pylint: disable=too-few-public-methods
class HttpResponse:

    def __init__(self, status_code, body) -> None:
        self.status_code = status_code
        if self.status_code == 200:
            self.body = body
        else:
            self.body = {
                "error": body
            }
