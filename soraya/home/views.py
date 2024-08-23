from django.shortcuts import render ,redirect
from django.views import View
from .models import AboutUs , FAQ , ContactUs , Supporter , MainSlider
from blog.models import Post
from .forms import ContactUsForms
from django.contrib import messages

# Create your views here.


class HomeView(View) :

    template_name = 'home/index-2.html'


    def setup(self , request , *args , **kwargs ) :
        self.supporter = Supporter.objects.all()
        self.blogs     = Post.objects.all()
        self.picture_slider = MainSlider.objects.first()
        return super().setup(request , *args , **kwargs )

    def get(self , request ) :
        return render(request , self.template_name , {'supporter' : self.supporter , 'picture_slider' : self.picture_slider , 'blogs' : self.blogs })

    def post(self , request ):
        return render(request , self.template_name , {'supporter' : self.supporter , 'picture_slider' : self.picture_slider  , 'blogs' : self.blogs })


class AboutUserView(View) :

    template_name = 'account/about-us.html'


    def setup(self , request , *args , **kwargs ) :
        self.data = AboutUs.objects.first()
        return super().setup(request , *args , **kwargs )

    def get(self , request ) :
        return render(request , self.template_name , {'data' : self.data } )


class FAQView(View) :

    template_name = 'account/faq.html'

    def setup(self , request , *args , **kwargs ) :
        self.data = FAQ.objects.all()
        return super().setup(request , *args , **kwargs )

    def get(self , request ) :
        return render(request , self.template_name , {'data':self.data } )


class ContactUsView(View) :


    contact_form  = ContactUsForms
    template_name = 'home/contact-us.html'


    def get(self , request ) :
        return render(request , self.template_name , {'form' : self.contact_form} )



    def post(self, request ) :
        form = self.contact_form(request.POST )
        if form.is_valid() :
            new_contact = form.save()
            messages.success(request , 'با موفقیت پیام شما ثبت شد' , 'success')
            return redirect('home:home')

        return render(request , self.template_name , {'form' : self.contact_form } )



class Error(View) :

    template_name = 'home/error-404.html'


    def get(self , request ) :
        return render(request , self.template_name , {} )


