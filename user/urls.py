from django.conf.urls import url, include
from . import views

urlpatterns = [url(r'add_student$', views.add_student, ), url(r'show_students$', views.show_students, ),
               url(r'get_student_data$', views.get_student_data, ), url(r'add_job$', views.add_job, ),
               url(r'add_company$', views.add_company, ), url(r'get_init_interest$', views.get_initial_interest, ),
               url(r'student_login$', views.student_login, ), url(r'company_login$', views.company_login, ),
               url(r'add_job$', views.add_job, ), url(r'add_resume$', views.add_resume, ),
               url(r'edit_resume$', views.edit_resume, ), url(r'show_job$', views.show_job, ),
               url(r'show_resume$', views.show_resume, ), url(r'show_recommend_jobs$', views.show_recommend_jobs, ), ]
