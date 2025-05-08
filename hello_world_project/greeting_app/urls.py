from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello, name = 'hello_view'),
    path('goodbye/', views.say_goodbye, name = 'goodbye_view')
]