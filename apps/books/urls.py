from rest_framework import routers
from django.urls import path

from apps.books import views

app_name = "apps.books"

urlpatterns = []

router = routers.SimpleRouter()
router.register("authors", views.AuthorModelViewSet)
router.register("books", views.BookModelViewSet)

urlpatterns += router.urls
