from django import forms

class HomeForm(forms.Form):
	name=forms.CharField()