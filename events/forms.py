from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'start_at',
            'end_at',
            'location',
            'organizer',
            'online_url',
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Назва події',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 6,
                    'placeholder': 'Опис події',
                }
            ),

            'start_at': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                },
                format='%Y-%m-%dT%H:%M',
            ),

            'end_at': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                },
                format='%Y-%m-%dT%H:%M',
            ),

            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Місце проведення',
                }
            ),

            'organizer': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),

            'online_url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'https://...',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['start_at'].input_formats = [
            '%Y-%m-%dT%H:%M'
        ]

        self.fields['end_at'].input_formats = [
            '%Y-%m-%dT%H:%M'
        ]

    def clean(self):
        cleaned_data = super().clean()

        start_at = cleaned_data.get('start_at')
        end_at = cleaned_data.get('end_at')

        if start_at and end_at and end_at < start_at:
            self.add_error(
                'end_at',
                'Дата завершення не може бути раніше дати початку.'
            )

        return cleaned_data
