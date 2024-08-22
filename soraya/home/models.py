from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class AboutUs(models.Model) :
    title = models.CharField(max_length=100 , verbose_name='درباره ما' )
    picture = models.FileField(upload_to='AboutUs/', verbose_name='تصویر درباره ما' )
    text1 = RichTextField(verbose_name= 'توضیحات 1' , null = True, blank = True )
    text2 = RichTextField(verbose_name='توضیحات 2' , null=True, blank=True )
    text3 = RichTextField(verbose_name='توضیحات 3 ' , null = True , blank=True )

    def __str__(self):
        return self.title


    class Meta :
        db_table = 'AboutUs'
        verbose_name_plural='درباره ما'
        ####

class FAQ(models.Model) :
    title = models.CharField(max_length=100 , verbose_name='عنوان سوال')
    text  = RichTextField(verbose_name='متن' )


    def __str__(self):
        return self.title


    class Meta :
        db_table = 'FAQ'
        verbose_name_plural='سوالات پر تکرار '




class ContactUs(models.Model) :

    STATUS_CHOICES = (
        ('pre' , 'بدون بررسی' ) , ('now' ,'در حال بررسی' ) , ('end' , 'تمام شده')
        )

    name   = models.CharField(verbose_name  = "نام" , max_length = 100 )
    family = models.CharField(verbose_name  = "نام خانوادگی" , max_length = 100 )
    email  = models.EmailField(verbose_name = "ایمیل"  )
    phone  = models.CharField(verbose_name  = 'شماره تلفن' , max_length = 11  , null = True )
    text   = models.TextField(verbose_name  = "متن"  )
    status = models.CharField(max_length = 20 , choices = STATUS_CHOICES ,default = 'pre' )

    def __str__(self ) :
        return f'{self.name} - {self.family} '


    class Meta :
        db_table = "ContactUs"
        verbose_name_plural = 'ارتباط با ما'


class Supporter(models.Model) :

    name    = models.CharField(verbose_name = 'نام حامی ما' , max_length = 100 )
    picture = models.FileField(verbose_name = 'لوگو' , upload_to = 'Supporter/' )


    def __str__(self ) :
        return self.name



    class Meta :
        db_table = 'Supporter'
        verbose_name_plural = 'Supporter'

