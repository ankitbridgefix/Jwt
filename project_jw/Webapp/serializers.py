from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from Webapp.models import Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = '__all__' 




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims, if needed
        token['username'] = user.username

        return token
    



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'