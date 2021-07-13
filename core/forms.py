from django import forms

class JoinForm(forms.Form): # or forms.ModelForm
    email = forms.EmailField(max_length=120)
    name = forms.CharField(max_length=120)