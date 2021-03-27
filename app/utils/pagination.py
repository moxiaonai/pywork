from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict

class GlobalPageNumberPagination(PageNumberPagination):
    def __init__(self):
        super(GlobalPageNumberPagination, self).__init__()
        self.page_size_query_param = 'page_size'
        self.max_page_size = 100  # 这个设置很重要

    def get_paginated_response(self, data):
        code = 200
        message = 'success'
        if not data:
            code = 404
            message = "Data Not Found"

        return Response(OrderedDict([
            ('code', code),
            ('message', message),
            ('count', self.page.paginator.count),
            ('total_pages', self.page.paginator.num_pages),
            ('data', data),
        ]))