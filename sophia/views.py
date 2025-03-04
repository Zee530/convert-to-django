from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def main(request):
    return render(request, 'index.html')

def program(request):
    return render(request, 'program.html')

def contact(request):
    return render(request, 'contact.html')

# def register(request):
#     return render(request, 'register.html')

def registerUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Registration.objects.create(
            name = name,		
            phone = phone,
            email = email,	
			message = message)
    
    return render(request,'register.html')

def apply(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        resume = request.FILES.get('resume')
        profile_pic = request.FILES.get('profile_pic')
        cover_letter = request.POST.get('cover_letter')
        JobApply.objects.create(
            full_name = full_name,
            email = email,
            resume = resume,
            profile_pic = profile_pic,
            cover_letter = cover_letter,
        )
        return redirect('main')
    return render(request, 'apply.html')
