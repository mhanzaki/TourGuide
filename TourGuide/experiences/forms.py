# forms.py
from django import forms

class SearchForm(forms.Form):
    destination = forms.CharField(label='Destination', max_length=100)
    category = forms.CharField(label='Category', max_length=100)