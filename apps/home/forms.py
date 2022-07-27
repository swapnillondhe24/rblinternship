from django import forms

# creating a form
class searchForm(forms.Form):
	title = forms.CharField()
