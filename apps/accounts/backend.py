from django.contrib.auth import get_user_model
from django.http import HttpRequest

User = get_user_model()


class EmailOrUsernameModelBackend(object):
    """
    This is a ModelBacked that allows authentication
    with an username or an email.

    """

    def authenticate(
        self, request: HttpRequest, username=None, password=None, **kwargs
    ):
        if "@" in username:
            kwargs = {"email": username}
        else:
            kwargs = {"username": username}
        try:
            user = User.objects.get(**kwargs)

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id: int):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
