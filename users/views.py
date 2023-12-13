from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserModel
from .serializers import CheckOPTSerializer, RegistrationSerializer, LoginSerializer
from rest_framework import status, generics, exceptions
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from .utils import send_otp_email, generate_otp


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        code = generate_otp()
        user.code = code
        user.save()

        send_otp_email(user.email, code)

        return Response({'message': 'Verification code has been sent to your email.'}, status=status.HTTP_200_OK)


class CheckOTPView(generics.GenericAPIView):
    serializer_class = CheckOPTSerializer

    def post(self, request, code):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        entered_code = serializer.validated_data.get('code')
        user = UserModel.objects.filter(code=code, is_verify=False).first()

        if not user or entered_code != user.code:
            raise exceptions.APIException('Code is incorrect!')

        if not user.is_verify:
            user.is_verify = True
            user.code = None
            user.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {'message': 'User is already verified.'}, status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = UserModel.objects.get(email=email)

            if not check_password(password, user.password):
                return Response(
                    {"error": "Неверный пароль."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            refresh = RefreshToken.for_user(user)
            return Response(
                {"refresh": str(refresh), "access": str(refresh.access_token)},
                status=status.HTTP_200_OK,
            )

        except UserModel.DoesNotExist:
            return Response(
                {"error": "Пользователь с этой почтой не существует."},
                status=status.HTTP_404_NOT_FOUND,
            )

