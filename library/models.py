from django.db import models
from django.template.defaultfilters import default
import datetime

class Books(models.Model):
    title = models.CharField('Titulo',max_length=100, blank=False)
    type = models.CharField('Tipo', max_length=40,blank=False)
    author = models.CharField('Autor', max_length=100,blank=False)
    creation_date = models.DateField('Fecha alta',null=False,default=datetime.datetime.now)
    number_of_pages=models.IntegerField(null=True)
    user=models.CharField(max_length=30,null=True)
    borrow_date= models.DateField('Fecha de prestamo',null=True)   # Create your models here.
