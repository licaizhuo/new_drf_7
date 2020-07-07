from rest_framework.views import exception_handler as lcz_exception_handler
from rest_framework import status
from utils.response import MyResponse


def exception_handler(exc, context):
    error = f"{context['view']}--{context['request'].method}--{exc}"
    print(error)
    response = lcz_exception_handler(exc, context)
    if response is None:
        return MyResponse(data_message="程序内部错误，请稍等一会~",
                          data_status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          exception=None)
    return response

