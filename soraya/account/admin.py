from django.contrib import admin
from .models import Profile
from django.utils.html import format_html
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):


    list_display = ('person' , 'phone' , 'code_melli' , 'img_show' , 'hb_show')

    def img_show(self , obj ):
        if obj.picture :

            return format_html('<img width="100px" heigth="100px" src="{}">'.format(obj.picture.url))
        else :
            return "No Image"

    img_show.short_description = 'تصویر کابر'


    def hb_show(self , obj ):
        if obj.hb :
            return obj.hb.strftime('%m/%d/%Y')
        else :
            return "No Hb "
    hb_show.short_description = 'تاریخ تولد'
