from django import forms
from .models import Project,BillOfMaterials,Service

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model=Project
        # exclude = ['created_at']
        fields=[
            'name',
            'quote',
            'adjust_bom',
            'adjust_service',
        ]

class BillModelForm(forms.ModelForm):
    class Meta:
        model=BillOfMaterials
        exclude = ['index']
        # fields={
        #     'name',
        #     # 'bom',
        #     # 'service',
        # }

class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude=['index','rate_list','rate_cost']






class ProjectForm(forms.Form):
    name=forms.CharField()
    quote=forms.IntegerField()
    adjusted_bom=forms.IntegerField()
    adjusted_service=forms.IntegerField()