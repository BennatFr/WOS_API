from django.http import JsonResponse

def custom_bad_request_view(request, exception):
    response_data = {
        "error": "Host not allowed",
        "message": "The host you are trying to access is not allowed. Please check the allowed hosts."
    }
    return JsonResponse(response_data, status=400)