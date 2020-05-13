from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from .models import Student, Job, Company, Resume
import random, string


# 学生注册
@require_http_methods(["GET"])
def add_student(request):
    response = {}
    try:
        student = Student(studentid=genRandomString(), sloginid=request.GET.get('sloginid'),
                          spassword=request.GET.get('spassword'), sname=request.GET.get('sname'),
                          sgrade=request.GET.get('sgrade'), sschool=request.GET.get('sschool'),
                          smajor=request.GET.get('smajor'))
        student.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 获取学生的初始兴趣
@require_http_methods(["GET"])
def get_initial_interest(request):
    response = {}
    try:
        sloginid_input = request.GET.get('sloginid')
        interest_input = request.GET.getlist('interest')
        student = Student.objects.get(sloginid=sloginid_input)
        student.interest = interest_input
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 学生登录
@require_http_methods(["GET"])
def student_login(request):
    response = {}
    try:
        sloginid_input = request.GET.get('sloginid')
        spassword_input = request.GET.get('spassword')
        spassword_db = Student.objects.get(sloginid=sloginid_input)
        if spassword_input == spassword_db:
            response['msg'] = 'success'
            response['error_num'] = 0
        else:
            response['msg'] = "password wrong"
            response['error_num'] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 2
    return JsonResponse(response)


# 公司注册
@require_http_methods(["GET"])
def add_company(request):
    response = {}
    try:
        company = Company(companyid=genRandomString(), cloginid=request.GET.get('cloginid'),
                          cpassword=request.GET.get('cpassword'), cname=request.GET.get('cname'),
                          ctel=request.GET.get('ctel'), caddress=request.GET.get('caddress'))
        company.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 公司登录
@require_http_methods(["GET"])
def company_login(request):
    response = {}
    try:
        cloginid_input = request.GET.get('cloginid')
        cpassword_input = request.GET.get('cpassword')
        cpassword_db = Company.objects.get(cloginid=cloginid_input)
        if cpassword_input == cpassword_db:
            response['msg'] = 'success'
            response['error_num'] = 0
        else:
            response['msg'] = "password wrong"
            response['error_num'] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 2
    return JsonResponse(response)


# 添加招聘信息
@require_http_methods(["GET"])
def add_job(request):
    response = {}
    try:
        # jobinfo = json.loads(request.GET.get('jobinfo'))
        job = Job(jobid=genRandomString(), jobinfo=request.GET.get('jobinfo'),
                  company_companyid=Company.objects.get(cloginid=request.GET.get('companyid')))
        job.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 添加简历
@require_http_methods(["GET"])
def add_resume(request):
    response = {}
    try:
        resume = Resume(resumeid=genRandomString(10),
                        student_studentid=Student.objects.get(sloginid=request.GET.get('studentid')),
                        sname=request.GET.get('sname'), sgrade=request.GET.get('sgrade'),
                        sschool=request.GET.get('sschool'),
                        smajor=request.GET.get('smajor'), skillinfo=request.GET.get('skillinfo'),
                        selfintro=request.GET.get('selfintro'),
                        tel=request.GET.get('tel'), email=request.GET.get('email'),
                        edubegin=request.GET.get('edubegin'), eduend=request.GET.get('eduend'),
                        cname=request.GET.get('cname'), industry=request.GET.get('industry'),
                        pname=request.GET.get('pname'),
                        place=request.GET.get('place'), expbegin=request.GET.get('expbegin'),
                        expend=request.GET.get('expend'))
        resume.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 编辑简历
@require_http_methods(["GET"])
def edit_resume(request):
    response = {}
    try:
        initial_resume = Resume.objects.get(
            student_studentid=Student.objects.get(sloginid=request.GET.get('studentid')))
        initial_resume.delete()
        resume = Resume(resumeid=genRandomString(10),
                        student_studentid=Student.objects.get(sloginid=request.GET.get('studentid')),
                        sname=request.GET.get('sname'), sgrade=request.GET.get('sgrade'),
                        sschool=request.GET.get('sschool'),
                        smajor=request.GET.get('smajor'), skillinfo=request.GET.get('skillinfo'),
                        selfintro=request.GET.get('selfintro'),
                        tel=request.GET.get('tel'), email=request.GET.get('email'),
                        edubegin=request.GET.get('edubegin'), eduend=request.GET.get('eduend'),
                        cname=request.GET.get('cname'), industry=request.GET.get('industry'),
                        pname=request.GET.get('pname'),
                        place=request.GET.get('place'), expbegin=request.GET.get('expbegin'),
                        expend=request.GET.get('expend'))
        resume.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 查看简历
@require_http_methods(["GET"])
def show_resume(request):
    response = {}
    try:
        sloginid_input = request.GET.get('sloginid')
        resume_db = Resume.objects.get(student_studentid=sloginid_input)
        response['sname'] = resume_db.sname
        response['sgrade'] = resume_db.sgrade
        response['sschool'] = resume_db.sschool
        response['smajor'] = resume_db.smajor
        response['skillinfo'] = resume_db.skillinfo
        response['selfintro'] = resume_db.selfintro
        response['tel'] = resume_db.tel
        response['email'] = resume_db.email
        response['edubegin'] = resume_db.edubegin
        response['eduend'] = resume_db.eduend
        response['cname'] = resume_db.cname
        response['industry'] = resume_db.industry
        response['pname'] = resume_db.pname
        response['place'] = resume_db.place
        response['expbegin'] = resume_db.expbegin
        response['expend'] = resume_db.expend
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 推荐招聘信息
@require_http_methods(["GET"])
def show_recommend_jobs(request):
    response = {}
    try:
        sloginid_input = request.GET.get('sloginid')
        # jobs = recommendation_by_tag(sloginid_input)
        jobs = {}
        i = 0
        for item in jobs:
            response[i] = Job.objects.get(jobid=item)
            i = i + 1
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 辅助函数
# this function is a test case for return value
@require_http_methods(["GET"])
def show_students(request):
    response = {}
    try:
        students = Student.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", students))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# this function is a test case for output data from database
@require_http_methods(["GET"])
def get_student_data(request):
    response = {}
    try:
        for data in Student.objects.all():
            print(data.sname)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def genRandomString(slen=10):
    return ''.join(random.sample(string.ascii_letters + string.digits, slen))
