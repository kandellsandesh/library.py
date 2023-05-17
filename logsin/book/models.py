from django.db import models

# Create your models here.

class Book(models.Model):  # models vaneko package ani Model vaneko models vitra ko library
   
    name=models.CharField(max_length=50)
    picture=models.ImageField()
    author=models.CharField(max_length=25,default='guest')
    email=models.EmailField(blank=True)
    description=models.TextField(default='Available in Lict Library',max_length=50)

    def __str__(self):
        return self.name
