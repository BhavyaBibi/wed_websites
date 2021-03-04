from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Destination(models.Model):
    
    groom= models.CharField(null=True,blank=True, max_length=50)
    bride= models.CharField(null=True,blank=True, max_length=50)
    groom_image = models.ImageField(upload_to='uploads/', verbose_name='image')
    bride_image = models.ImageField(upload_to='uploads/', verbose_name='image')
    descrption = RichTextField(blank=True, null=True)
    date = models.DateField()

