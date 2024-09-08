from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer

@api_view(['POST'])
def register(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Compte créé avec succès"})
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = CustomUser.objects.filter(email=email).first()
    if user is None:
        return Response({"message": "User not found"}, status=404)
    if not user.check_password(password):
        return Response({"message": "Wrong password"}, status=400)
    return Response({"message": "Login successful"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)

# Exemple d'action réservée aux développeurs
from rest_framework.permissions import BasePermission

class IsDeveloppeur(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.metier == 'dev'

@api_view(['GET'])
@permission_classes([IsDeveloppeur])
def developpeur_only_action(request):
    return Response({"message": "Cette action est réservée aux développeurs."})