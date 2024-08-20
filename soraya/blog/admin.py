from django.contrib import admin
from .models import Post , Category_Blog
from django.utils.html import format_html

# Register your models here.


@admin.register(Post)
class Post_Admin(admin.ModelAdmin) :
    list_display = ('name' , 'slug' , 'category' , 'show_img' )

    prepopulated_fields = {'slug':('name' , )}


    def show_img(self, obj ) :
        return format_html('<img width=50px heigth=50px src="{}">'.format(obj.picture.url))


    show_img.short_description  = 'تصویر پست'


@admin.register(Category_Blog)
class Category_Blog_Admin(admin.ModelAdmin) :
    list_display = ('name' , 'slug' )
    prepopulated_fields = {'slug':('name' , )}