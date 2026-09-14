from django import forms

from .models import ForumMessage, ForumTopic


class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ['title', 'text']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Назва теми',
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 7,
                    'placeholder': 'Текст першого повідомлення',
                }
            ),
        }


class ForumMessageForm(forms.ModelForm):
    class Meta:
        model = ForumMessage
        fields = ['text']

        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Ваше повідомлення',
                }
            ),
        }