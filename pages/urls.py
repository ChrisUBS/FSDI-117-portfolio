from django.urls import path
from pages import views

urlpatterns = [
    path("", views.HomePageView, name="home"),
    path("about/", views.AboutPageView, name="about"),
    path("contact/", views.ContactPageView, name="contact"),
]