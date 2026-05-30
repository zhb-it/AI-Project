from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """ 用户注册序列化器 """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'date_of_birth', 'avatar', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    """ 用户信息序列化器 """
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'date_of_birth', 'avatar']

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance