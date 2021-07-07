"""projecthotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('registration/',views.registration),
    #path('/design/',views.design),
    path('registrationdata',views.registrationdata),
    #path('regidata',views.regidata),
    #path('login/',views.login),
    #path('logindata',views.logindata),
    path('regi/',views.regi),
    path('regidata',views.regidata),
    path('login/', views.login),
    path('logindata',views.logindata),
    path('index',views.index),
    path('form/',views.form),
    path('formdata',views.formdata),
    path('data',views.data),
    path('edit',views.edit),
    path('update/<productid>',views.update),
    path('updatedata',views.updatedata),
    path('INEEX',views.INEEX),
    path('child',views.child)





]
