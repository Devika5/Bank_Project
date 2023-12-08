from . import views
from django.urls import path

urlpatterns = [
     path('',views.index,name='home'),
     path('register/', views.register, name='register'),
     path('login/',views.login,name='login'),
     path('new/', views.new, name='new'),
     path('form/',views.form, name='form'),
     path('index/', views.index, name='index'),
     # path('wikipedia/', views.wikipedia, name='wikipedia'),

     ]
