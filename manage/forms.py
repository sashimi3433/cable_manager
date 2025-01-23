from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Item, CustomUser
from hashlib import sha256
import time
from django.core.exceptions import ValidationError

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
            'image':'画像',
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

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # 1. 画像ファイルの拡張子を確認
            allowed_extensions = ['jpg','jpeg','png']
            # ファイル名から拡張子を取得し小文字に変換
            file_extension = image.name.lower().split('.')[-1]
            print("file_extension",file_extension)
            if not any(file_extension.endswith(ext) for ext in allowed_extensions):
                raise ValidationError("JPEGまたはPNGフォーマットの画像ファイルをアップロードしてください。")
            # 2. ファイル名をハッシュ化
            time_int = int(time.time())
            hashed_filename = sha256(image.name.encode()).hexdigest()[:10] # ファイル名をハッシュ化して10文字までにする
            image.name = f"{hashed_filename}{str(time_int)}.{file_extension}" # 新しいファイル名をハッシュ値 + タイムスタンプ + 拡張子に設定
        return image