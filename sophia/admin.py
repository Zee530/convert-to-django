from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available')
    list_filter = ('available', 'price')
    search_fields = ['name'] 
    list_editable = ('price', 'stock', 'available')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone','email','message')
    list_filter = ('name','email')
    search_fields = ['name', 'email']

class JobApplyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'cover_letter', 'applied_on', 'resume', 'profile_pic')
    list_filter = ('full_name', 'applied_on')
    search_fields = ['full_name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(JobApply, JobApplyAdmin)
