from django import forms
from .models import List




class ItemList(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]
         
        