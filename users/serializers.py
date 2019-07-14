from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserSerializer(UserListSerializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    date_joined = serializers.ReadOnlyField()


class WriteUserSerializer(UserSerializer):

    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate_username(self, value):
        has_to_check_username = self.instance is not None and self.instance.username != value
        if has_to_check_username and User.objects.filter(username=value).exists():
            raise ValidationError('The username {0} is already used'.format(value))
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Passwords do not match')
        return attrs

    def create(self, validated_data):
        user = User()
        return self.update(user, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.set_password(validated_data.get('password'))
        instance.email = validated_data.get('email')
        instance.save()
        return instance