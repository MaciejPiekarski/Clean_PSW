"""
Definition of models.
"""

from django.db import models
from django.forms import widgets
from django.contrib.auth.models import User

# Create your models here.


class Services(models.Model):

    #contener = models.ForeignKey(Commands, verbose_name="Kontener")
    sql = models.CharField('Serwer baz danych',max_length=50,default='Brak')
    http = models.CharField('Serwer http',max_length=50,default='Brak')
    php = models.CharField('Serwer php',max_length=50,default='Brak')

    class Meta:
        verbose_name = 'Usługa'
        verbose_name_plural = 'Usługi'

    def __str__(self):
        return self.sql


class Commands(models.Model):
    
    ip = models.CharField('IP', max_length=25)
    system = models.CharField('System', max_length=50)
    ram = models.IntegerField('Ram')
    quote = models.IntegerField('Quote')
    name = models.CharField('Nazwa', max_length=8)
    user = models.ForeignKey(User, verbose_name="Użytkownik")
    services = models.ForeignKey(Services,null= True, verbose_name="Usługi")

    class Meta:
        verbose_name = 'Komenda'
        verbose_name_plural = 'Komendy'

    def __str__(self):
        return self.name




