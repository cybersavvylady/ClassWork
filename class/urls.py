#
# This is the project urls file, must not have any reference to admin
# Each app needs to have a default path
from django.urls import path
from . import views

app_name = "class"
urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("add/", views.add, name="add"),
    path("viewdata/", views.viewdata, name="viewdata"),
]
