from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from . import forms

app_name = 'core'

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/', views.contact, name='contact'), 
    path('singup/', views.singup, name='singup'), 
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=forms.loginForm), name='login'),
]
