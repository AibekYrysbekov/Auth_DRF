from django.contrib.auth import authenticate
from rest_framework import serializers


from .models import UserModel


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = UserModel
        fields = ['email', 'password', 'username']

    @staticmethod
    def validate_email(value):
        user = UserModel.objects.filter(email=value)
        if user.exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel.objects.create_user(**validated_data, password=password)
        return user


class CheckOPTSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField()

    class Meta:
        model = UserModel
        fields = ['code']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials')
        else:
            raise serializers.ValidationError('Must include "email" and "password"')


