from django import forms
from .models import Product
from config.forms import StyleFormMixin

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
    'бесплатно', 'обман', 'полиция', 'радар'
]


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name').lower()
        for word in FORBIDDEN_WORDS:
            if word in name:
                raise forms.ValidationError(f'Название не может содержать слово "{word}".')
        return self.cleaned_data.get('name')

    def clean_description(self):
        description = self.cleaned_data.get('description').lower()
        for word in FORBIDDEN_WORDS:
            if word in description:
                raise forms.ValidationError(f'Описание не может содержать слово "{word}".')
        return self.cleaned_data.get('description')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")

        return price


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ["description", "owner"]
