from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.authentication import JWTAuthentication
from api.filter import MyFilter, ComputerFilterSet
from api.models import Computer
from api.paginations import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination
from api.serializers import UserModelSerializer, ComputerModelSerializer
from utils.response import MyResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


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
        return MyResponse(data_message="成功", results=UserModelSerializer(user_ser.obj).data, token=user_ser.token)


class ComputerListAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer

    # filter_backends = [SearchFilter, OrderingFilter]
    # filter_backends = [SearchFilter]
    # search_fields = ["name", 'price']

    # ordering = ['-price']
    # pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination
    filter_backends = [MyFilter, DjangoFilterBackend]
    search_fields = ["name", 'price']
    filter_class = ComputerFilterSet
