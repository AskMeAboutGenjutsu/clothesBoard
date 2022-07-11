from django import forms
from django.core.exceptions import ValidationError
from .models import EBordModel, CategoryModel
from captcha.fields import CaptchaField
from django.core import validators


class EBordForm(forms.ModelForm):
    title = forms.CharField(
        label='Название товара',
        max_length=15, required=True,
        help_text='Введите название товара',
    )
    content = forms.CharField(
        label='Описание товара',
        widget=forms.Textarea(),
        required=True,
        help_text='Введите описание товара',
    )
    price = forms.DecimalField(
        label='Цена товара',
        decimal_places=2,
        required=True,
        min_value=0,
        max_digits=8,
        help_text='Введите цену товара в руб.'
    )
    category = forms.ModelChoiceField(
        queryset=CategoryModel.objects.all(),
        label='Категория товара',
        help_text='Выберите категорию товара',
        widget=forms.Select(),
    )
    image = forms.ImageField(
        label='Изображение товара',
        validators=[validators.FileExtensionValidator(
            allowed_extensions=('gif', 'png', 'jpg'))],
        error_messages={'invalid_extension': 'Этот формат не поддерживается'},
        widget=forms.FileInput
    )

    captcha = CaptchaField(
        label='Введите текст с картинки',
        error_messages={'invalid': 'Неправильный текст'}
    )

    class Meta:
        model = EBordModel
        fields = ('title', 'content', 'price', 'category', 'image', 'captcha')


