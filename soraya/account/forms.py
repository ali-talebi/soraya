from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class LoginForm(forms.Form) :

    username = forms.CharField()
    password = forms.CharField()



class SignUpForm(forms.Form) :
    full_name = forms.CharField()
    email     = forms.EmailField()
    password  = forms.CharField()
    confirm_password = forms.CharField()
    phone = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()




    def clean_email(self):
        new_email = self.cleaned_data['email']

        user = User.objects.filter(email = new_email ).exists()
        if user :
            raise ValidationError('ایمیل قبلا ثبت نام شده است')


        return new_email


    def clean_confirm_password(self):
        new_conf_password = self.cleaned_data['confirm_password']
        new_password      = self.cleaned_data['password']
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password'] and self.cleaned_data['password'] and self.cleaned_data['confirm_password']  :
            raise ValidationError('رمز عبور با رمز تایید مطابقت ندارد')

        return new_conf_password







