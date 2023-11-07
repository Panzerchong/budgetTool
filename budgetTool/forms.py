from django import forms
from .models import Project

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude = ['created_at']
        fields={
            'name',
            'quote',
            # 'bom',
            # 'service',
        }

class ProjectForm(forms.Form):
    name=forms.CharField()
    quote=forms.IntegerField()