from user.models import Users
from rest_framework import viewsets, permissions
from . serializers import UsersSerializer

# User Viewset
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsersSerializer