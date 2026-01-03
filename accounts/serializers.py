from rest_framework import serializers
from django.contrib.auth import get_user_model
from organizations.models import Organization

User = get_user_model()

class SignupSerializer(serializers.Serializer):
    organization_name = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # 1️⃣ Create Organization
        organization = Organization.objects.create(
            name=validated_data["organization_name"]
        )

        # 2️⃣ Create Admin User
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            role="ADMIN",
            organization=organization
        )

        return user
