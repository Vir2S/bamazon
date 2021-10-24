from rest_framework import routers
from django.urls import path

from apps.books import views

app_name = "apps.books"

urlpatterns = [
    path("books/", views.BookGenericListAPIView.as_view()),
    path("books/create/", views.BookGenericCreateAPIView.as_view()),
    path("authors/", views.AuthorGenericListAPIView.as_view()),
    path("authors/create/", views.AuthorGenericCreateAPIView.as_view()),
]

# router = routers.SimpleRouter()
# router.register("authors", views.AuthorModelViewSet)
# router.register("books", views.BookModelViewSet)
# router.register("authors", views.AuthorGenericListAPIView)
# router.register("books", views.BookGenericListAPIView)


# urlpatterns += router.urls
