from django import forms
from .models import *

class TestForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'test', 'question_name']
        
