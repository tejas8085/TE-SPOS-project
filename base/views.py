from django.shortcuts import render
from .models import  Contact


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'base/index.html')

# def contact(request):
#      return render(request, 'base/contact.html')
 
def contact(request):
    if request.method == "POST":
     
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'base/contact.html')

def about(request):
    return HttpResponse("We are at about")



def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")

