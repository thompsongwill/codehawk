from .models import List
from django import forms 



class ItemList(forms.ModelForm):
    class meta:
        model = List
        fields = ["item", "completed"]
         
        