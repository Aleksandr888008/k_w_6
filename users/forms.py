from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, PasswordResetForm, \
    SetPasswordForm, UsernameField
from django import forms
from transliterate.utils import _

from mailing.forms import FormStyleMixin
from users.models import User


class UserRegisterForm(FormStyleMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(FormStyleMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'avatar',)
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class CustomAuthenticationForm(FormStyleMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class CustomPasswordResetForm(FormStyleMixin, PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User


class CustomResetConfirmForm(SetPasswordForm):
    class Meta:
        model = User