"""
URL configuration for athena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from manager import views

app_name = "manager"

urlpatterns = [
    path('', views.loginuser, name='loginuser'),
    path('/home', views.home, name='home'),
    path('/logout', views.logoutuser, name='logoutuser'),
    path('/<int:pk>', views.details, name='details'),
    path('/answer/<int:pk>', views.answer, name='answer'),
    path('/addquestion', views.add_question, name='add_question'),
    path('/cv', views.cvanalysis, name='cvanalysis'),
    path('/genprofile', views.gen_profile, name='genprofile'),
    path('/positions', views.positions, name='positions'),
    path('/positions/detail/<int:pk>', views.pos_details, name='pos_details'),
    path('/generator/questions/', views.gen_questions, name='gen_questions'),
    path('/generator/linkedin/', views.linkedin, name='linkedin'),
    path('/transcript', views.transcript, name='transcript'),
    path('/generator/questions/technical', views.technical, name='technical'),
]
