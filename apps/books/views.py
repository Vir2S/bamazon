from rest_framework import viewsets, generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser

from apps.books.models import Author, Book
from apps.books.serializers import AuthorSerializer, BookSerializer
from apps.books.permissions import ActionBasedPermission


class AuthorModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAdminUser: ["update", "partial_update", "destroy", "create"],
        AllowAny: ["list", "retrieve"]
    }


class BookModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (ActionBasedPermission,)
    pagination_class = LimitOffsetPagination
    action_permissions = {
        IsAdminUser: ["update", "partial_update", "destroy", "create"],
        AllowAny: ["list", "retrieve"]
    }
