from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Select, Textarea, EmailInput, PasswordInput, TimeInput

from .models import ExamProcess


class ExamForm(forms.ModelForm):
    class Meta:
        model = ExamProcess

        fields = ['exam_name', 'exam_question_set', 'start_time', 'end_time']

        exclude = ['exam_user', 'date', 'active_status']

        widgets = {

            'exam_name': Select(attrs={'class': 'form-control'}),
            'exam_question_set': Select(attrs={'class': 'form-control'}),
            'start_time': TimeInput(attrs={'class': 'form-control'}),
            'end_time': TimeInput(attrs={'class': 'form-control'}),

        }






