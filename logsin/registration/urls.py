from django.urls import path
from . import views

urlpatterns=[
    path('',views.signup,name='signup'),
    path('login',views.loginpage,name='login'),
    #path('home',views.home,name="home"),
    path('logout',views.logoutpage,name='logout'),
    path('email',views.send_template_email,name='email'),



]

