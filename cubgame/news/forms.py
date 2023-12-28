from django.contrib.auth.models import User
from.models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django import  forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'dost', "fault", 'full_text', 'date']

        widgets = {
            "dost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Достоинство'
            }),
            "fault": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Недостатки"
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'

            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст отзыва'
            })
        }
