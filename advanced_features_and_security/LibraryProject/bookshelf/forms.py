from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

class ExampleForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)