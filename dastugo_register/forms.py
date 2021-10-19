from django import forms
from crispy_forms.helper import FormHelper
from django.forms import fields
from .models import Student

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        # fields = "__all__"
        exclude = ['register_date','last_update_date']
        labels = {
            'first_name': ('Adı (Türkçe site için)'),
        }
        help_texts = {
            'first_name': ('Bu iki alana öğrencinin adını ve soyadını giriniz.'),
        }
        error_messages = {
            'first_name': {
                'max_length': ("Bu isim çok uzun."),
            },
        }