from django import forms

from catalog.models import Product

forbidden_phrases = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

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
