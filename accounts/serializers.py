from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'is_seller', 'is_buyer', 'token']

    def validate(self, data):
        is_buyer = data.get('is_buyer', False)
        is_seller = data.get('is_seller', False)

        if not is_buyer and not is_seller:
            raise serializers.ValidationError("User must be either a buyer or a seller.")
        if is_buyer and is_seller:
            raise serializers.ValidationError("User cannot be both buyer and seller.")
        
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data.get('username', ''),
            is_seller=validated_data.get('is_seller', False),
            is_buyer=validated_data.get('is_buyer', False),
            password=make_password(password)
        )
        return user

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
