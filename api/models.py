from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=40)
    price= models.IntegerField()
    discount = models.IntegerField(default=0)
    duration = models.FloatField()



# Create your models here.
