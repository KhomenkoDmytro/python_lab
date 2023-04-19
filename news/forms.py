from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announcement', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of the article',
                'required': 'true'
            }),
            "announcement": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Announcement',
                'required': 'true'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of publication',
                'required': 'true'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Content of the article',
                'required': 'true'
            }),
        }
