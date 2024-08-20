from django.db import models
from ckeditor.fields import  RichTextField
# Create your models here.



class Category_Blog(models.Model) :
    name = models.CharField(verbose_name = 'نام دسته بندی' , max_length=100  , unique = True )
    slug = models.SlugField(verbose_name = 'آدرس دسته بندی'  )


    def __str__(self ) :
        return self.name



    class Meta :
        db_table = 'Category_Blog'
        verbose_name_plural = 'دسته بندی های وبلاگ'


class Post(models.Model) :

    picture = models.FileField(verbose_name = '' , upload_to = 'blog/Post/' )
    name = models.CharField(max_length   = 100 , verbose_name = 'عنوان دسته بندی' )
    slug = models.SlugField(verbose_name = 'آدرس اینترنتی' )
    category    = models.ForeignKey(Category_Blog , on_delete = models.CASCADE , related_name = 'post' , verbose_name = 'دسته بندی ' )
    description1 = RichTextField(verbose_name = 'توضیحات' , blank = True )
    description2 = RichTextField(verbose_name = 'توضیحات' , blank = True , null = True  )




    def __str__(self) :
        return self.name


    class Meta :
        db_table = 'Post'
        verbose_name_plural = 'پست های وبلاگ'






