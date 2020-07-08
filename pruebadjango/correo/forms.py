from django import forms

class RegForm(forms.Form):
	correo_form = forms.CharField(max_length=100)
	edad = forms.CharField(max_length=50)
