from django.contrib import admin
from .models import AboutUs , FAQ , ContactUs
# Register your models here.
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title' , )



@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title' , )

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin) :
    list_display  = ('name' , 'family' , 'email' , 'phone' , 'status' )
    list_editable = ('status' , )
    search_fields = ('name' , 'family' , 'email' , 'phone' )
    list_filter   = ('status' , )