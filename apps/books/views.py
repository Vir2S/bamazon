from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import AllowAny

from apps.books.models import Author, Book
from apps.books.serializers import AuthorSerializer, BookSerializer


class AuthorModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)


class BookModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    pagination_class = LimitOffsetPagination
