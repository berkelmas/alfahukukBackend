
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class YayinlarPagePagination(PageNumberPagination):
    page_size = 4
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'totalpages': self.page.paginator.num_pages,  ## get number of total pages
            'results': data
        })

class YayinlarPageOthersPagination(PageNumberPagination):
    page_size= 6
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'totalpages': self.page.paginator.num_pages,
            'results': data
        })
