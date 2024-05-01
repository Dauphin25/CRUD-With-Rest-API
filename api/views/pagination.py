from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 2 # Default page size
    page_size_query_param = 'page_size'
    max_page_size = 100 # Maximum page size
