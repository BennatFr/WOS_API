from rest_framework.views import APIView
from rest_framework.response import Response
class APIDetailsView(APIView):
    def get(self, request):
        data = {
            "version": "1.0",
            "creator": "Bennat"
        }
        return Response(data)
