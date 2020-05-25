from django.conf.urls import url, include
from . import views

urlpatterns = [url(r'add_student$', views.add_student, ), url(r'show_students$', views.show_students, ),
               url(r'get_student_data$', views.get_student_data, ), url(r'add_job$', views.add_job, ),
               url(r'add_company$', views.add_company, ), url(r'get_init_interest$', views.get_initial_interest, ),
               url(r'student_login$', views.student_login, ), url(r'company_login$', views.company_login, ),
               url(r'add_job$', views.add_job, ), url(r'add_resume$', views.add_resume, ),
               url(r'edit_resume$', views.edit_resume, ), url(r'show_job$', views.show_job, ),
               url(r'show_resume$', views.show_resume, ), url(r'get_recommend_jobs$', views.get_recommend_jobs, ),
               url(r'get_recommend_talks$', views.get_recommend_talks, ), url(r'show_company$', views.show_company, ),
               url(r'get_my_job$', views.get_my_job, ), url(r'deliver_resume$', views.deliver_resume, ),
               url(r'attend_talk$', views.attend_talk, ), url(r'get_my_talk$', views.get_my_talk, ),
               url(r'interview$', views.interview, ), url(r'show_interview$', views.show_interview, ),
               url(r'add_companyForm$', views.add_companyForm, ), url(r'show_companyForm$', views.show_companyForm, ),
               url(r'show_seminar_students$', views.show_seminar_students, ), url(r'return_jobs$', views.return_jobs, ),
               url(r'return_resumes$', views.return_resumes, ), url(r'add_seminar$', views.add_seminar, ),
               url(r'add_job$', views.add_job, ), url(r'show_students$', views.show_students, ), ]
