from django import forms

class OrderForms(forms.form):
    name = forms.CharField( max_length=200, required=False)
    phone = forms.CharField( max_length=200, required=False)