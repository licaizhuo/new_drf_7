import re

from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer
from rest_framework_jwt.settings import api_settings

from api.models import User, Computer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class UserModelSerializer(ModelSerializer):
    account = serializers.CharField(write_only=True)
    pwd = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # fields = ("username", "pwd")
        # fields = ("account", "pwd")
        fields = ("account", "pwd", "username", "phone", "email")
        extra_kwargs = {
            # "username": {
            #     "required": True,
            # },
            # "password": {
            #     "required": True,
            #     "write_only": True,
            # }

            "username": {
                "read_only": True,
            },
            "phone": {
                "read_only": True,
            },
            "email": {
                "read_only": True,
            }
        }

    def validate(self, attrs):
        # username = attrs.get("account")
        # password = attrs.get("pwd")
        # print(username)
        # print(password)
        # user_obj = User.objects.filter(username=username).first()
        # print(attrs)
        # print(user_obj)
        # if user_obj:
        #     payload = jwt_payload_handler(user_obj)
        #     token = jwt_encode_handler(payload)
        #     print(payload)
        #     print(token)
        account = attrs.get("account")
        pwd = attrs.get("pwd")
        if re.match(r'.+@.+', account):
            user_obj = User.objects.filter(email=account).first()
        elif re.match(r'1[3-9][0-9]{9}', account):
            user_obj = User.objects.filter(phone=account).first()
        else:
            user_obj = User.objects.filter(username=account).first()
        if user_obj and user_obj.check_password(pwd):
            payload = jwt_payload_handler(user_obj)
            token = jwt_encode_handler(payload)
            self.token = token
            self.obj = user_obj
        else:
            raise exceptions.ValidationError("请输入正确的用户名或密码")
        return attrs


class ComputerModelSerializer(ModelSerializer):
    class Meta:
        model = Computer
        fields = ('name', 'price', 'brand')
