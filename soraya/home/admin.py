from django.contrib import admin
from .models import AboutUs , FAQ , ContactUs , Supporter , MainSlider
from django.utils.html import format_html
# Register your models here.





@admin.register(MainSlider)
class MainSlider_Admin(admin.ModelAdmin) :
    list_display = ('name' ,  'img_show'  )


    def img_show(self , obj) :
        return "1"
    img_show.short_description = 'تصویر '

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title' , )




@admin.register(Supporter)
class SupporterAdmin(admin.ModelAdmin) :
    list_display = ('name' ,  )





@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title' , )



@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin) :
    list_display  = ('name' , 'family' , 'email' , 'phone' , 'status' )
    list_editable = ('status' , )
    search_fields = ('name' , 'family' , 'email' , 'phone' )
    list_filter   = ('status' , )