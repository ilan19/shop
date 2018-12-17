from django.urls import path
from . import views

app_name = 'contact_app'

urlpatterns = [
  path('contactform', views.contactform, name='contactform'),
  path('contactform/success', views.success, name='success'),
]
