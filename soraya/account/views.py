from django.shortcuts import render , redirect
from django.views import View
from .forms import LoginForm , SignUpForm
from .models import Profile
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.





class SignUpView(View):
    signup_form = SignUpForm
    template_name = 'account/register.html'

    def get(self ,request ) :
        return render(request , self.template_name , {'form' : self.signup_form } )


    def post(self ,request ) :
        form = self.signup_form(request.POST)
        if form.is_valid() :

            n_email    = form.cleaned_data['email']
            n_password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            n_phone = form.cleaned_data['phone']
            n_city = form.cleaned_data['city']
            n_country = form.cleaned_data['country']
            user_created = User.objects.create_user(username = n_email.split("@")[0] , email = n_email ,password = n_password )
            profile_created = Profile(person = user_created , phone =  n_phone , address = n_country + ' - ' + n_city )
            profile_created.save()
            return redirect('home:home')
            messages.success ( request , 'با موفیت ثبت نام انجام شد' , 'success')

        else :
            messages.error ( request , 'مشكلي در ثبت نام به وجود آمده است' , 'error')


        return render(request , self.template_name , {'form' : self.signup_form } )

class LoginView(View):




    login_form = LoginForm
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            return redirect('home:home')

        return super().dispatch(request, *args, **kwargs)

    def get(self ,request ):
        return render(request, self.template_name , {'form' : self.login_form} )


    def post(self  ,request ):
        form = self.login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password )
            if user :
                login(request , user )
                messages.success(request, 'با موفقیت وارد شدید'  , 'success')
                return redirect('home:home')

            else :
                messages.error(request , 'مشکلی در ورود دارید' , 'error')



        return render(request, self.template_name , {'form' : self.login_form} )



class LogoutView(View) :

    def get(self , request ):
        logout(request)
        return redirect('home:home')