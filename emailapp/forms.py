from .views import *
from django import forms

class profileform(forms.Form):
    name=forms.CharField(max_length=10)
    price = forms.DecimalField(max_digits=10, decimal_places=2)


#forms--->django html page
class ContactusForm(forms.Form):
    Name=forms.CharField(max_length=10)
    Email=forms.EmailField()
    Message=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows':3,'cols':30}))
