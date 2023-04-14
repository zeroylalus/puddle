from django import forms
from . import models

class NewItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ('category', 'name', 'description', 'price', 'image')