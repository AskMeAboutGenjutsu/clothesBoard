from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import CaptchaField
from .models import UserProfileModel
from django.core import validators


class UserRegForm(UserCreationForm):
    username = forms.CharField(
        max_length=10,
        label='Логин пользователя',
        help_text='Введите логин',
        required=True
    )
    email = forms.EmailField(
        label='Электронная почта пользователя',
        help_text='Введите электронную почту',
        required=True
    )
    first_name = forms.CharField(
        label='Имя',
        help_text='Введите ваше имя',
    )
    last_name = forms.CharField(
        label='Фамилия',
        help_text='Введите вашу фамилию',
    )
    password1 = forms.CharField(
        label='Пароль пользователя',
        help_text='Пароль не должен быть менее 8 и более 32 символов',
        widget=forms.widgets.PasswordInput,
        max_length=32,
        min_length=8,
        required=True
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        help_text='Введите пароль',
        widget=forms.widgets.PasswordInput,
        max_length=32,
        min_length=8,
        required=True
    )
    captcha = CaptchaField(
        label='Введите текст с картинки',
        error_messages={'invalid': 'Неправильный текст'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'captcha')


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        max_length=10,
        label='Изменить логин',
        help_text='Введите логин',
        required=True
    )
    email = forms.EmailField(
        label='Изменить электронную почту',
        help_text='Введите электронную почту',
        required=True
    )
    first_name = forms.CharField(
        label='Изменить имя',
        help_text='Введите ваше имя',
    )
    last_name = forms.CharField(
        label='Изменить фамилию',
        help_text='Введите вашу фамилию',
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class UserUpdateProfileForm(forms.ModelForm):
    image = forms.ImageField(
        label='Изменить изображение',
        validators=[validators.FileExtensionValidator(
            allowed_extensions=('gif', 'png', 'jpg'))],
        error_messages={'invalid_extension': 'Этот формат не поддерживается'},
        widget=forms.FileInput
    )
    city = forms.CharField(
        label='Изменить город',
        max_length=15,
    )

    class Meta:
        model = UserProfileModel
        fields = ('image', 'city')


