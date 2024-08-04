from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version

forbidden_phrases = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('created_by', )

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        for phrase in forbidden_phrases:
            if phrase in cleaned_data:
                raise forms.ValidationError('Запрещенное выражение в названии!')

        return cleaned_data

    def clean_desc(self):
        cleaned_data = self.cleaned_data.get('desc')

        for phrase in forbidden_phrases:
            if phrase in cleaned_data:
                raise forms.ValidationError('Запрещенное выражение в описании!')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
