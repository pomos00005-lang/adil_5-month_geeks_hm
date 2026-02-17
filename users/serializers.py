from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError



class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 150)
    password = serializers.CharField()


    def validate_username(self,username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')

class ConfirmcodeSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    code = serializers.CharField(max_length=6)

    def validate_data(self, code, username):
        try:
            user = User.objects.get(username=username)
            if user.code == code:
                user.is_active = True
            else:
                raise ValidationError('не правильный код')
        except User.DoesNotExist:
            raise ValidationError('user is not found')
        return user
