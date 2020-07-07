from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPageNumberPagination(PageNumberPagination):
    #    每页的数量
    page_size = 2
    # 设置页数的查询参数，可以不设置，默认就为page
    page_query_param = "page"
    # page_query_param = "ppp"
    # 指定每页的个数，
    # 再继承简单的以页数分页的这个类（基础分页器），想要修改每页的个数，必须指定查询参数
    # 如果不指定，默认为None
    page_size_query_param = "page_size"
    # 指定每页显示的最大数量，
    # 即使page_size_query_param = "page_size"通过这个参数指定多大，
    # 最大都不会超过max_page_size
    max_page_size = 3


class MyLimitOffsetPagination(LimitOffsetPagination):
    # 默认获取每页的数量
    default_limit = 2
    # 指定查询参数，可以修改每页的数量,
    # 可以不指定，默认就是limit
    limit_query_param = "limit"
    # limit_query_param = "ppp"
    # 偏移量，可以不指定，默认就是offset
    offset_query_param = "offset"
    # offset_query_param = "ooo"
    # 每页的最大数量
    max_limit = 3


class MyCursorPagination(CursorPagination):
    # 默认获取每页的数量
    page_size = 2
    # 指定每页的个数，
    # 再继承简单的以页数分页的这个类（基础分页器），想要修改每页的个数，必须指定查询参数
    # 如果不指定，默认为None
    page_size_query_param = "page_size"
    # 默认为None
    max_page_size = 3
    # ordering = "name"
    # 可以不指定，默认就是cursor_query_param = 'cursor'
    # cursor_query_param = "cursor"

