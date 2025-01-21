from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Item, CustomUser

class DateInput(forms.DateInput):
    input_type = 'date'

class RegForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
        self.fields["date"].widget.attrs["max"] = "9999-12-31"

    class Meta:
        model = Item
        exclude = ['user']  # userフィールドを除外
        labels={
            'name':'商品名',
            'date':'購入日',
            'Manufacturer':'メーカー',
            'Store':'販売店',
            'length':'長さ',
            'watt':'ワット数',
            'PD':'PD',
            'thunderbolt':'thunderbolt',
            'comment':'備考',
        }
        widgets = {
            'date': DateInput(),
        }