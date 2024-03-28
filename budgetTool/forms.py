from django import forms
from .models import BOMCategory, Product_Price, Project,BillOfMaterials, RateTable,Service, ServiceCategory,RateTableCost, Vendor
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
            "sales_price":forms.NumberInput(attrs={'title': 'Leave blank to get default price or enter custom price','placeholder':"List price",'style': 'width: 100px;'}),
            "quantity":forms.NumberInput(attrs={'placeholder':"Quantity",'style': 'width: 85px;'}),
            "supplier":forms.TextInput(attrs={'placeholder':"Supplier",'style': 'width: 85px;'}),
            "actual_cost":forms.NumberInput(attrs={'placeholder':"Cost (Actual)",'style': 'width: 100px;'}),
            "Responsible":forms.TextInput(attrs={'placeholder':"Responsible",'style': 'width: 100px;'}),
            "description":forms.TextInput(attrs={'placeholder':"Description",'style': 'width: 100px;'}),
            "notes":forms.TextInput(attrs={'placeholder':"Notes",'style': 'width: 200px; height: 30px;'}),
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
            "isOnSite": forms.CheckboxInput(attrs={'style': 'width: 50px;'}),
            "hours_estimated":forms.NumberInput(attrs={'placeholder':"Hours(Estimate)",'style': 'width: 120px;'}),
            "hours_worked":forms.NumberInput(attrs={'placeholder':"Hours(Worked)",'style': 'width: 120px;'}),
            "notes":forms.TextInput(attrs={'placeholder':"Notes",'style': 'width: 200px; height: 30px;'}),
            # "rate_list":forms.NumberInput(attrs={'placeholder':"Rate List",'style': 'width: 100px;'}),
            # "rate_cost":forms.NumberInput(attrs={'placeholder':"Rate Cost ",'style': 'width: 100px;'}),
            "travel_actual":forms.NumberInput(attrs={'placeholder':"Travel Actual",'style': 'width: 100px;'}),
            "project":forms.HiddenInput(),
            "rate_list":forms.HiddenInput(),
            "rate_cost":forms.HiddenInput(),
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
        
class RateCostModelForm(forms.ModelForm):
    class Meta:
        model = RateTableCost
        fields = '__all__'
        widgets = {  
            "name": forms.TextInput(attrs={'placeholder':"Name"}),
            "code": forms.TextInput(attrs={'placeholder':"Code"}),
            "base": forms.NumberInput(attrs={'placeholder':"Base"}),
            "y1": forms.NumberInput(attrs={'placeholder':"Y1"}),
            "y2": forms.NumberInput(attrs={'placeholder':"Y2"}),
            "y3": forms.NumberInput(attrs={'placeholder':"Y3"}),
            "y4": forms.NumberInput(attrs={'placeholder':"Y4"}),
            "labor_cost": forms.NumberInput(attrs={'placeholder':"Labor Cost"}),    
            "labor_rate_in_house": forms.NumberInput(attrs={'placeholder':"Labor Rate(In House)"}),
            "labor_rate_on_site": forms.NumberInput(attrs={'placeholder':"Labor Rate(On Site)"}),
            "employee": forms.TextInput(attrs={'placeholder':"Employee"}),
        }

class ProductPriceModelForm(forms.ModelForm):
    class Meta:
        model = Product_Price
        fields = '__all__'
        widgets = {
            "item": forms.TextInput(attrs={'placeholder':"Item"}),
            "cost": forms.NumberInput(attrs={'placeholder':"Cost"}),
            "list": forms.NumberInput(attrs={'placeholder':"List"}),
            "note": forms.TextInput(attrs={'placeholder':"Note"}),
        }

class VendorModelForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        widgets = {
            "index": forms.NumberInput(attrs={'placeholder':"#",'style': 'width: 50px;'}),
            "name": forms.TextInput(attrs={'placeholder':"Name"}),
        }

class UserForm(UserCreationForm):
	# email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	