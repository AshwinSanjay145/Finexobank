from .import views
from django.urls import path, include

app_name='user'
urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
]
