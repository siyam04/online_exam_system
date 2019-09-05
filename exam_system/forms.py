from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Select, Textarea, EmailInput, PasswordInput, TimeInput

from .models import Questions


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions

        fields = '__all__'

        widgets = {

            'name': TextInput(attrs={'class': 'form-control'}),
            'option_1': TextInput(attrs={'class': 'form-control'}),
            'option_2': TextInput(attrs={'class': 'form-control'}),
            'option_3': TextInput(attrs={'class': 'form-control'}),
            'option_4': TextInput(attrs={'class': 'form-control'}),

        }




