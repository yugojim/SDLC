"""sdlc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from . import views
app_name = 'sdlc'
urlpatterns = [
    path('', views.index, name='index'),
    path('issues/', views.issues, name='issues'),
    
    path('sdlc1/', views.sdlc1, name='sdlc1'),
    path('sdlc2/', views.sdlc2, name='sdlc2'),
    path('sdlc3/', views.sdlc3, name='sdlc3'),
    path('sdlc4/', views.sdlc4, name='sdlc4'),
    path('sdlc5/', views.sdlc5, name='sdlc5'),
    path('sdlc6/', views.sdlc6, name='sdlc6'),
    
    path('admin/', admin.site.urls),    
    path('accounts/', include('django.contrib.auth.urls')),
]