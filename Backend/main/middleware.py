from django.core.exceptions import DisallowedHost
from django.http import JsonResponse

class CustomHostValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except DisallowedHost:
            response_data = {
                "error": "Host not allowed",
                "message": "The host you are trying to access is not allowed. Please check the allowed hosts."
            }
            return JsonResponse(response_data, status=400)
        return response
