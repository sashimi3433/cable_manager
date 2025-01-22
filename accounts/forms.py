from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")
        labels={
            'username':'ユーザーネーム',
            'email':'メールアドレス',
            'password1':'パスワード',
            'password2':'パスワード (確認用)',
        }