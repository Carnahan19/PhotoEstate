"""
URL configuration for PhotoE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.tasks, name='task'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('virtualstaging/', views.vstagin, name='virtualstaging'),
    path('enhancements/', views.enhancements, name='enhancements'),
    path('twilight/', views.twilight, name='twilight'),
    path('floorplans/', views.floorplans, name='floorplans'),
    path('njobs/', views.njobs, name='njobs'),
    path('orders/', views.orders, name='orders'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'tasks.views.handler404'
