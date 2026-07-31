from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("photography/", views.photography, name="photography"),
    path("fashion/", views.fashion, name="fashion"),
    path("travel/", views.travel, name="travel"),
    path("single/", views.single, name="single"),
]