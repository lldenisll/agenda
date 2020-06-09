"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.list_events), #route
    path('agenda/list/<int:id_user>/', views.jason_list_event),
    path('agenda/event/',views.event),
    path('agenda/event/submit', views.submit_event),
    path('agenda/event/delete/<int:id_evento>/',views.delete_event),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/',views.login_user),
    path('login/submit', views.submit_login),
    path('logout/',views.logout_user),

]
