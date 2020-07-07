import jwt
from rest_framework import exceptions
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_decode_handler


class JWTAuthentication(BaseJSONWebTokenAuthentication):
    def authenticate(self, request):

        token = self.get_jwt_value(request)
        if token is None:
            return None
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed("签名已过期")
        except:
            raise exceptions.AuthenticationFailed("非法用户")

        user = self.authenticate_credentials(payload)

        return user, token

    def get_jwt_value(self, request):
        jwt_values = request.META.get("HTTP_AUTHORIZATION")
        if not jwt_values:
            return None
        tokens = jwt_values.split()
        if len(tokens) != 3 or tokens[0].lower() != "auth" or tokens[2].lower() != "jwt":
            return None
        return tokens[1]
