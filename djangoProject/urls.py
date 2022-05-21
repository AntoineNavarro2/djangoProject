"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from lycee import views
from lycee.views import StudentCreateView, ParticularCallCreateView

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('lycee/', views.index, name='home'),
    path('lycee/student/<int:student_id>', views.detail_student, name='detail_student'),
    path('lycee/student/update/<int:student_id>', views.update_student, name='update_student'),
    path('lycee/presence/<int:presence_id>', views.detail_presence, name='detail_presence'),
    path('lycee/student/create', StudentCreateView.as_view(), name='create_student'),
    path('lycee/presence/call', ParticularCallCreateView.as_view(), name='create_presence_part'),
    path('lycee/presence/curususcall/<int:cursus_id>', views.cursus_call, name='create_presence'),
    path('lycee/cursus/<int:cursus_id>', views.detail_cursus, name='detail_cursus'),
    path('lycee/presence/', views.detail_all_presence, name='detail_all_presence'),
]