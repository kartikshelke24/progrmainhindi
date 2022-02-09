
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.loginForm,name='loginForm'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logoutHandle,name='logoutHandle'),
]