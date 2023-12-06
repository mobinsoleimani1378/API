from rest_framework import serializers

from .models import User, Otp


class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'fullname', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            phone=validated_data['phone'],
            fullname=validated_data['fullname'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class OtpSer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = ('token',)
