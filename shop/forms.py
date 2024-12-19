from django import forms
from .models import Pendant

class PendantForm(forms.ModelForm):
    class Meta:
        model = Pendant
        fields = ['name', 'description', 'price', 'image', 'group']
