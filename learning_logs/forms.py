from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
            'class': 'form-control',  # Применяем класс Bootstrap
            'placeholder': 'Enter topic name'  # Плейсхолдер
        })


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',  # Применяем класс Bootstrap
                'rows': 5,  # Высота текстового поля
                'placeholder': 'Write your entry here...'  # Плейсхолдер
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
