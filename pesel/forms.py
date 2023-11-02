from django import forms
from .models import Pesel


class PeselForm(forms.ModelForm):
    class Meta:
        model = Pesel
        fields = ('pesel',)
