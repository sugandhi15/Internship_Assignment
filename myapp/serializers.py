from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password  


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # write_only ensures that field is only write and cannot be readed

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password']) 
        return super().create(validated_data)