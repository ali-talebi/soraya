from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
# Create your models here.



class Profile(models.Model) :

    person     = models.OneToOneField(User , related_name='profile_related', verbose_name= 'کاربر'    ,  on_delete=models.CASCADE  )
    phone      = models.CharField(max_length = 100 , verbose_name='شماره تلفن' , null = True , blank = True )
    picture    = models.FileField(upload_to='Profile/Picture/' ,  null = True , blank = True   )
    code_melli = models.CharField(max_length=10 , null = True , blank = True )
    hb = jmodels.jDateTimeField(verbose_name='تاریخ تولد' , null = True , blank=True )
    address = models.TextField(verbose_name='آدرس منزل' , null = True , blank = True )








    @property
    def select_full_name(self ):
        _s  = ''
        if self.person.first_name :
            _s += f'{self.person.first_name} - '

        if self.person.last_name :
            _s += f'{self.person.last_name}'

        return _s

    def __str__(self):
        if len(self.select_full_name) != 0   :
            return self.select_full_name


        return f'{self.person.username}'

    class Meta :
        db_table = 'Profile'
        verbose_name_plural = 'مشخصات دقیق حساب کاربری'