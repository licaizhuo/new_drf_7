from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.views import obtain_jwt_token

from api import views

urlpatterns = [
    # path('login/', obtain_jwt_token),
    path('user/', views.UserAPIView.as_view()),
    # path('login/', ObtainJSONWebToken.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('cps/', views.ComputerListAPIView.as_view()),
]
