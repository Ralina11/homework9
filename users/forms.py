from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import EmailField

from main.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        # fields = ('email', 'password1', 'password2')
        fields = ('email',)
        field_classes = {'email':EmailField}


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()