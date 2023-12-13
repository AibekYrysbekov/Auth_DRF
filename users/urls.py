from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users.views import RegistrationView, CheckOTPView, LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('confirm-email/<str:code>/', CheckOTPView.as_view(), name='confirm-email'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
