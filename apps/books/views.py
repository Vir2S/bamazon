from rest_framework import viewsets, generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser

from apps.books.models import Author, Book
from apps.books.serializers import AuthorSerializer, BookSerializer


# class AuthorModelViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing accounts.
#     """
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     permission_classes = (AllowAny,)
#
#
# class BookModelViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing accounts.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (AllowAny,)
#     pagination_class = LimitOffsetPagination


class AuthorGenericListAPIView(generics.ListAPIView):
    """
    A simple Generic List API View for viewing authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)
    pagination_class = LimitOffsetPagination


class AuthorGenericRetrieveAPIView(generics.RetrieveAPIView):
    """
    A simple Generic List API View for retrieve single author's details.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)


class AuthorGenericCreateAPIView(generics.CreateAPIView):
    """
    A simple Generic Create API View for creating authors.
    """
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminUser,)


class BookGenericListAPIView(generics.ListAPIView):
    """
    A simple Generic List API View for viewing books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    pagination_class = LimitOffsetPagination


class BookGenericRetrieveAPIView(generics.RetrieveAPIView):
    """
    A simple Generic List API View for retrieve single book's details.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)


class BookGenericCreateAPIView(generics.CreateAPIView):
    """
    A simple Generic Create API View for creating books.
    """
    serializer_class = BookSerializer
    permission_classes = (IsAdminUser,)
