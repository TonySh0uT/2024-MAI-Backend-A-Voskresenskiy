"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('cws', views.cws, name='cws'),
    path('cw/<uuid:cw_id>', views.cw, name='cw'),
    path('cw/search', views.search_cw, name='search_cw'),
    path('cw/create', views.create_cw, name='create_cw'),
    path('students', views.students, name='students'),
    path('student/<uuid:student_id>', views.student, name='student'),
    path('student/create', views.create_student, name='create_student'),
    path('advisers', views.advisers, name='advisers'),
    path('adviser/<uuid:adviser_id>', views.adviser, name='adviser'),
    path('adviser/create', views.create_adviser, name='create_adviser'),
]
