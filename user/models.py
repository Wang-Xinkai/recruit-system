# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Company(models.Model):
    companyid = models.CharField(primary_key=True, max_length=10)
    cloginid = models.CharField(max_length=10, blank=True, null=True)
    cpassword = models.CharField(max_length=45, blank=True, null=True)
    cname = models.CharField(max_length=10, blank=True, null=True)
    ctel = models.CharField(max_length=45, blank=True, null=True)
    caddress = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Job(models.Model):
    jobid = models.CharField(primary_key=True, max_length=10)
    companyid = models.CharField(max_length=10, blank=True, null=True)
    jobinfo = models.TextField(blank=True, null=True)  # This field type is a guess.
    company_companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_companyid')
    resume_resumeid = models.ForeignKey('Resume', models.DO_NOTHING, db_column='resume_resumeid')

    class Meta:
        managed = False
        db_table = 'job'


class Jobhistory(models.Model):
    student_studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='student_studentid')
    job_jobid = models.ForeignKey(Job, models.DO_NOTHING, db_column='job_jobid')

    class Meta:
        managed = False
        db_table = 'jobhistory'
        unique_together = (('student_studentid', 'job_jobid'),)


class LoginUser(models.Model):
    name = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=256)
    email = models.CharField(unique=True, max_length=254)
    sex = models.CharField(max_length=32)
    c_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'login_user'


class Resume(models.Model):
    resumeid = models.CharField(primary_key=True, max_length=10)
    sname = models.CharField(max_length=10, blank=True, null=True)
    sgrade = models.IntegerField(blank=True, null=True)
    sschool = models.CharField(max_length=45, blank=True, null=True)
    smajor = models.CharField(max_length=45, blank=True, null=True)
    eduinfo = models.TextField(blank=True, null=True)  # This field type is a guess.
    interninfo = models.TextField(blank=True, null=True)  # This field type is a guess.
    skillinfo = models.TextField(blank=True, null=True)  # This field type is a guess.
    selfintro = models.TextField(blank=True, null=True)  # This field type is a guess.
    student_studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='student_studentid')

    class Meta:
        managed = False
        db_table = 'resume'


class Seminar(models.Model):
    seminarid = models.CharField(primary_key=True, max_length=10)
    companyid = models.CharField(max_length=10, blank=True, null=True)
    stime = models.DateTimeField(blank=True, null=True)
    splace = models.CharField(max_length=45, blank=True, null=True)
    stheme = models.CharField(max_length=45, blank=True, null=True)
    company_companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_companyid')

    class Meta:
        managed = False
        db_table = 'seminar'


class Seminarhistory(models.Model):
    student_studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='student_studentid')
    seminar_seminarid = models.ForeignKey(Seminar, models.DO_NOTHING, db_column='seminar_seminarid')

    class Meta:
        managed = False
        db_table = 'seminarhistory'
        unique_together = (('student_studentid', 'seminar_seminarid'),)


class Student(models.Model):
    studentid = models.CharField(primary_key=True, max_length=10)
    sloginid = models.CharField(max_length=10, blank=True, null=True)
    spassword = models.CharField(max_length=45, blank=True, null=True)
    sname = models.CharField(max_length=10, blank=True, null=True)
    sgrade = models.IntegerField(blank=True, null=True)
    sschool = models.CharField(max_length=45, blank=True, null=True)
    smajor = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
