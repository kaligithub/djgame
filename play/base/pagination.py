from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination


class GamePageNumberPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 30

    page_query_param = 'page_no'
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return OrderedDict(
            [
                ('count', self.page.paginator.count),
                ('current', self.page.number),
                ('next', self.get_next_link()),
                ('previous', self.get_previous_link()),
                ('total_pages', self.page.paginator.num_pages),
                ('results', data),
            ]
        )
