"""Softphone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    ######################################Home Page####################################################
    path('', index, name='index'),

    ######################################URLS#########################################################
    path('loginUser/', loginUser, name='loginUser'),
    path('logoutUser/', logoutUser, name='logoutUser'),

    ######################################ADMIN URLS#########################################################
    path('adminDashboard/', adminDashboard, name='adminDashboard'),
    path('createClientAccount/', createClientAccount, name='createClientAccount'),



    ######################################AGENT URLS#########################################################
    path('agentDashboard/', agentDashboard, name='agentDashboard'),
    path('createNewAgent/', createNewAgent, name='createNewAgent'),
    
]
