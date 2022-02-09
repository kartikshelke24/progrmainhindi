from django.db import models


# Create your models here.

class Contact(models.Model):
    sno= models.AutoField(primary_key=True) 
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=50)
    phone_num = models.CharField(max_length=13)
    message = models.TextField() 
    date_time = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name