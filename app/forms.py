from app.models import *
from django import forms

class CollegeForm(forms.ModelForm):
    class Meta:
        model=College
        fields='__all__'

