from django.shortcuts import render
from .models import New


# Create your views here.
from django.http import HttpResponse
def News(request):
    
    searchTerm = request.GET.get('searchNew')
    if searchTerm:
         news = New.objects.filter(title__icontains=searchTerm)
    else:
         news = New.objects.all()
    return render(request,"newss.html",{'searchTerm':searchTerm,'news':news})
def  signups(request):
     return render(request,'signups.html')