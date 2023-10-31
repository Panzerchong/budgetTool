from django import forms

class ProjectForm(forms.Form):
    name=forms.CharField()
    quote=forms.IntegerField()