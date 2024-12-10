from django import forms
from .models import GooglePass

class GoogleForm(forms.ModelForm):
    class Meta:
        model = GooglePass
        fields = ['email', 'password']