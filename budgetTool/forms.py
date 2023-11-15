from django import forms
from .models import Project,BillOfMaterials,Service

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model=Project
        # exclude = ['created_at']
        fields=[
            'name',
            'quote_BOM',
            'quote_Service',
            'adjust_BOM',
            'adjust_Service',
            'travel_weekly',
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
        exclude=[
            'hours_adjusted',
            'travel_estimate',
            'sub_total_list',
            'sub_total_adjusted_list',
            'sub_total_cost_est',
            'sub_total_adjusted_cost_est',
            'cost_actual',
        ]






class ProjectForm(forms.Form):
    name=forms.CharField()
    quote_BOM=forms.IntegerField()
    quote_Service=forms.IntegerField()
    adjusted_bom=forms.IntegerField()
    adjusted_service=forms.IntegerField()