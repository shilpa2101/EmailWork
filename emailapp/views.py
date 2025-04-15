from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core.mail import send_mail
from emailpro.settings import EMAIL_HOST_USER
# Create your views here.

def admins(request):
    if request.method=='POST':
        a=profileform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            pr=a.cleaned_data['price']
            b=profile(name=nm,price=pr)
            b.save()
            return HttpResponse("success")
        else:
            print(a.errors)
            return HttpResponse("failed")
    else:
        return render(request,'main.html')
    
def contact(request):
    sub=ContactusForm()  
    return render(request,'contactus.html',{'form':sub})

def contactus_view(request):
    sub=ContactusForm()
    if request.method=='POST':
        sub=ContactusForm(request.POST)
        if sub.is_valid():
            email=sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message=sub.cleaned_data['Message']
            send_mail(str(name)+'||'+str(email),message,EMAIL_HOST_USER,[email],fail_silently=False)
            return render(request,'contactussuccess.html')
    return render(request,'contactus.html',{'form':sub})    

