from django.shortcuts import render
from .models import Movie

# Create your views here.
from django.http import HttpResponse
def home(request):
    searchTerm=request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request,"home.html",{'searchTerm':searchTerm,'movies':movies})
def signup(request):
    email=request.GET.get('email')
    return render(request,"signup.html",{'email':email})
