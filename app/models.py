from django.db import models

# Create your models here.

from django.urls import reverse
class School(models.Model):
    Scname=models.CharField(max_length=100)
    Scprincipal=models.CharField(max_length=100)
    Sclocation=models.CharField(max_length=100)

    def __str__(self):
        return self.Scname
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Student(models.Model):
    stname=models.CharField(max_length=100)
    stage=models.IntegerField()
    scname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')




    