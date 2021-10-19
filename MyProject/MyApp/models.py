from django.db import models


# Create your models here.s
class Feature(models.Model):
    name=models.CharField(max_length=100,default='fast')
    details= models.CharField(max_length=500,default='we are amazing')
    
    def __str__(self):
        return self.name


    
    