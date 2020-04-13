from rest_framework import serializers
from user.models import Users

# User serializer
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"