from .import views
from django.urls import path, include


urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name="profile"),
    path("application/", views.application, name="application"),
    path("application/load_cities/", views.load_cities, name="load_cities")


]
