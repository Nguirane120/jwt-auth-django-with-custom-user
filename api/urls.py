from django.urls import path, re_path
from . import views
from .views import MyTokenObtainPairView
from .views import RegisterView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoute),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/register', RegisterView.as_view()),
]