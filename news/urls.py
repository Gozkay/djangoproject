from django.urls import path
from .import views

urlpatterns = [
    path('',views.News, name='news'),
    path('signups',views.signups, name='signups'),


]