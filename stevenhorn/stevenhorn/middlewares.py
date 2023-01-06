
class VictorinaMiddleware:
    def __init__(self, get_responce):
        self.get_responce = get_responce

    def __call__(self, request, *args, **kwargs):
        responce = self.get_responce(request, *args, **kwargs)
        return responce