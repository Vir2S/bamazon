from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import CustomUser

User = get_user_model()


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = ("email", "password", "phone", "password_expire_at")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password", "phone", "password_expire_at")


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"name": "email", "placeholder": "Email"}
        ),
        label="Email",
    )

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        )


class AuthenticationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"name": "username", "placeholder": "Username/Email"}
        ),
        label="Username/Email",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"name": "password", "placeholder": "Password"}
        ),
        label="Password",
    )

    class Meta:
        fields = ("password", "username")


class UserPasswordResetForm(PasswordResetForm):
    """Overwrite PasswordResetForm to enable password restore by username"""

    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={"name": "username", "placeholder": "Username/Email"}
        ),
        label="Username/Email",
    )

    def get_users(self, email: str):
        """Given an email, return matching user who should receive a reset."""
        if "@" in email:
            try:
                return User.objects.get(email=email)
            except User.DoesNotExist:
                return None
        else:
            try:
                return User.objects.filter(username=email).first()
            except User.DoesNotExist:
                return None

    def save(
        self,
        domain_override=None,
        subject_template_name="registration/password_reset_subject.txt",
        email_template_name="registration/password_reset_email.html",
        use_https=False,
        token_generator=default_token_generator,
        from_email=None,
        request=None,
        html_email_template_name=None,
        extra_email_context=None,
    ):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        email = self.cleaned_data["email"]
        if not domain_override:
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
        else:
            site_name = domain = domain_override

        email_field_name = User.get_email_field_name()
        user = self.get_users(email)
        if user is not None:
            user_email = getattr(user, email_field_name)
            context = {
                "email": user_email,
                "domain": domain,
                "site_name": site_name,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                "token": token_generator.make_token(user),
                "protocol": "https" if use_https else "http",
                **(extra_email_context or {}),
            }
            self.send_mail(
                subject_template_name,
                "account/password_reset_email.html",
                context,
                from_email,
                user_email,
                html_email_template_name=html_email_template_name,
            )
            messages.success(request, "Check your mail dude")
        else:
            messages.error(request, "Oh damn we didn't find you")
