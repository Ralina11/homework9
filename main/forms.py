from django import forms

from main.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']  # список запрещенных слов
        for word in forbidden_words:
            # Проверяем, содержит ли название или описание запрещенное слово
            if word in name.lower() or word in description.lower():
                # Если содержит, генерируем исключение с сообщением об ошибке
                raise forms.ValidationError(f'Слово "{word}" запрещено в названии и описании продукта.')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'