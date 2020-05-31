from django.db import models

# Create your models here.
class News(models.Model):
    new_name    =   models.CharField(max_length= 1000)
    new_author  =   models.CharField(max_length= 100)
    new_intro   =   models.TextField(max_length=300)
    new_des     =   models.TextField()
    new_count   =   models.PositiveSmallIntegerField(default=0)
    new_intro_pic   = models.ImageField(upload_to='new_pictures')