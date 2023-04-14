from django.contrib.auth import views as auth_views
from django.urls import path

from .views import index, contact, singup
from .forms import loginForm

app_name = 'core'

urlpatterns = [
    path('',index,name='index'),
    path('contact/', contact, name='contact'), 
    path('singup/', singup, name='singup'), 
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=loginForm), name='login'),
]
