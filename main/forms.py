from django import forms

from main.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "is_current_version":
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'  # Все поля
        # fields = ('name_prod', 'description_prod', 'img_prod')
        exclude = ('user_boss',) # поля которые исключаются

    def clean_name_prod(self):
        cleaned_data = self.cleaned_data['name_prod']

        if cleaned_data.title() in ['Казино', 'Криптовалюта', 'Крипта', 'Биржа', 'Дешево', 'Бесплатно', 'Обман', 'Полиция',
                        'Радар']:
            raise forms.ValidationError('Ой, всё, запрещенное слово')

        return cleaned_data

    def clean_description_prod(self):
        cleaned_data = self.cleaned_data['description_prod']

        if cleaned_data.title() in ['Казино', 'Криптовалюта', 'Крипта', 'Биржа', 'Дешево', 'Бесплатно', 'Обман', 'Полиция',
                        'Радар']:
            raise forms.ValidationError('Ой, всё, запрещенное слово')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
        # fields = ('name_prod', 'description_prod', 'img_prod')
        # exclude = () # поля которые исключаются




