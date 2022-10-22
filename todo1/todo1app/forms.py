from django import forms
from .models import UserForm,Company




class UserForm(forms.ModelForm):
    class Meta:
        model=UserForm
        fields = ["name","username","Email","mobile","password"]


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name","address"]
