from django.db import models

# Create your models here.

class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    short_desc=models.CharField(max_length=300,default='')
    
    content=models.TextField()
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField( max_length=50)
    phone=models.CharField(max_length=10)
    desc=models.TextField()
    time=models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name

