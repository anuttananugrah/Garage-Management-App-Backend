from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model:Customer
        fields="__all__"
        read_only_fields=["mechanic"]

class Serviceserializer(serializers.ModelSerializer):
    class Meta:
        model=Services
        fields="__all__"
        read_only_fiels=["customer","created_at"]