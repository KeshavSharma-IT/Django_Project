from django.urls import path
# in place of MyApp we can also place a .
from MyApp import views

urlpatterns=[
    path('',views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path ('logout', views.logout, name='logout'),
    path('post/<str:pk>',views.post, name='post')
    ]
