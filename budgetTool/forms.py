from django import forms
from .models import BOMCategory, Project,BillOfMaterials, RateTable,Service, ServiceCategory
from django.utils.translation import gettext_lazy as _

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
        fields="__all__"
        labels = {
            "index": _(""),
            "name": _(""),
            "estimate_cost": _(""),
            "sales_price": _(""),
            "quantity": _(""),
            "supplier": _(""),
            "actual_cost": _(""),
            "Responsible": _(""),
            "description": _(""),
            "notes": _(""),
            "bom_category": _("Category"),
            "project": _(""),
        }
        # help_texts = {
        #     "name": _("Some useful help text."),
        # }

        widgets = {
            "index": forms.NumberInput(attrs={'placeholder':"#",'style': 'width: 50px;'}),  
            "name": forms.TextInput(attrs={'placeholder':"Part/Item"}),  
            "estimate_cost":forms.NumberInput(attrs={'placeholder':"Cost(Estimate)",'style': 'width: 100px;'}),
            "sales_price":forms.NumberInput(attrs={'placeholder':"List price",'style': 'width: 100px;'}),
            "quantity":forms.NumberInput(attrs={'placeholder':"Quantity",'style': 'width: 85px;'}),
            "supplier":forms.TextInput(attrs={'placeholder':"Supplier",'style': 'width: 85px;'}),
            "actual_cost":forms.NumberInput(attrs={'placeholder':"Cost (Actual)",'style': 'width: 100px;'}),
            "Responsible":forms.TextInput(attrs={'placeholder':"Responsible",'style': 'width: 100px;'}),
            "description":forms.TextInput(attrs={'placeholder':"Description",'style': 'width: 100px;'}),
            "notes":forms.TextInput(attrs={'placeholder':"Notes",'style': 'width: 70px;'}),
        }


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
        labels = {
            "type": _("Type"),
            "rate_list": _("Rate List"),
            "rate_cost": _("Rate Cost"),
            "category": _("Category"),
            "isOnSite": _("Is on Site?"),
        }

        widgets = {
            "index": forms.NumberInput(attrs={'placeholder':"#",'style': 'width: 50px;'}),  
            "name": forms.TextInput(attrs={'placeholder':"Task"}),
            "type": forms.Select(attrs={'placeholder':"Type",'style': 'width: 100px;'}),
            "isOnSite": forms.CheckboxInput(attrs={'style': 'width: 50px;'}),
            "hours_estimated":forms.NumberInput(attrs={'placeholder':"Hours(Estimate)",'style': 'width: 120px;'}),
            "hours_worked":forms.NumberInput(attrs={'placeholder':"Hours(Worked)",'style': 'width: 120px;'}),
            "rate_list":forms.NumberInput(attrs={'placeholder':"Rate List",'style': 'width: 100px;'}),
            "rate_cost":forms.NumberInput(attrs={'placeholder':"Rate Cost ",'style': 'width: 100px;'}),
            "travel_actual":forms.NumberInput(attrs={'placeholder':"Travel Actual",'style': 'width: 100px;'}),
            "project":forms.HiddenInput(),
        }

class ProjectForm(forms.Form):
    name=forms.CharField()
    quote_BOM=forms.IntegerField()
    quote_Service=forms.IntegerField()
    adjusted_bom=forms.IntegerField()
    adjusted_service=forms.IntegerField()

class OrderForm(forms.Form):
   ordering=forms.CharField()

class BomCategoryModelForm(forms.ModelForm):
    class Meta:
        model = BOMCategory
        fields = '__all__'
        widgets = {
            "index": forms.NumberInput(attrs={'placeholder':"#",'style': 'width: 50px;'}),  
            "name": forms.TextInput(attrs={'placeholder':"Name"}),  }
        
class ServiceCategoryModelForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = '__all__'
        widgets = {
            "index": forms.NumberInput(attrs={'placeholder':"#",'style': 'width: 50px;'}),  
            "name": forms.TextInput(attrs={'placeholder':"Name"}),  }