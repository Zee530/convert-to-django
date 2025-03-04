from django.db import models
# from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Null')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)

class Registration(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(default=0)
    email = models.EmailField(unique=False)
    message = models.CharField(max_length=255)

class JobApply(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    cover_letter = models.TextField(default='No cover letter attached')
    applied_on = models.DateTimeField(auto_now_add=True)

