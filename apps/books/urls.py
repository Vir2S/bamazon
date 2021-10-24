from rest_framework import routers

from apps.books import views

app_name = "apps.books"

router = routers.SimpleRouter()
router.register("authors", views.AuthorModelViewSet)
router.register("books", views.BookModelViewSet)


urlpatterns = [] + router.urls
