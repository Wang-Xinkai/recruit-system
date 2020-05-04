from django.conf.urls import url, include
from . import views

urlpatterns = [url(r'add_student$', views.add_student, ), url(r'show_students$', views.show_students, ), ]
