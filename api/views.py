from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.authentication import JWTAuthentication
from api.serializers import UserModelSerializer
from utils.response import MyResponse


class UserAPIView(APIView):
    # authentication_classes = [JSONWebTokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        print("Love you is not two or three days")
        return MyResponse()


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user_ser = UserModelSerializer(data=request.data)
        user_ser.is_valid(raise_exception=True)
        return MyResponse(data_message="成功", results=UserModelSerializer(user_ser.obj).data,token=user_ser.token)
