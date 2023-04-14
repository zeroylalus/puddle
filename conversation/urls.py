from django.urls import path
from .views import new_conversation

app_name = 'conversation'

urlpatterns = [
    path('new/<int:item_pk>', new_conversation, name='new'),
]