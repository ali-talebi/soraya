from django import forms
from .models import ContactUs



class ContactUsForms(forms.ModelForm) :

    class Meta :
        model  = ContactUs
        fields = ['name' , 'family' , 'email' , 'phone'  , 'text' ]