from django.conf.urls import url, include
from . import views

urlpatterns = [url(r'add_student$', views.add_student, ), url(r'show_students$', views.show_students, ),
               url(r'get_student_data$', views.get_student_data, ), url(r'add_job$', views.add_job, ),
               url(r'add_company$', views.add_company, ), ]
