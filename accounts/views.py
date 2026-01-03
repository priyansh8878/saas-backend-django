from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import SignupSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from common.throttles import LoginRateThrottle

class TestProtectedView(APIView):
    def get(self, request):
        return Response({
            "message": "JWT authentication successful",
            "user": request.user.username,
            "role": request.user.role
        })

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "message": "Organization and admin user created successfully",
            "username": user.username,
            "organization": user.organization.name
        }, status=201)

class LoginView(TokenObtainPairView):
    throttle_classes = [LoginRateThrottle]