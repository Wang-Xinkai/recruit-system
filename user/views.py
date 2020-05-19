from enum import Enum

from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from .models import Student, Job, Company, Resume, Seminar
import random, string

max_pop = 0
MAX_INTEREST_LENGTH = 5


# 学生注册
# 学生id为随机生成的长度为10的字符串，为伪主键（可能出现重复）。
# 之后为简化实现，均使用 sloginid（注册id）作为主键进行查询
@require_http_methods(["GET"])
def add_student(request):
    response = {}
    try:
        # 新建学生
        student = Student(studentid=genRandomString(), sloginid=request.GET.get('sloginid'),
                          spassword=request.GET.get('spassword'), sname=request.GET.get('sname'),
                          sgrade=request.GET.get('sgrade'), sschool=request.GET.get('sschool'),
                          smajor=request.GET.get('smajor'), interest="", stel="")
        student.save()
        # 根据注册填写信息初始化一份简历
        resume = Resume(resumeid=genRandomString(10), sname=student.sname, sgrade=student.sgrade,
                        sschool=student.sschool, smajor=student.smajor,
                        student_studentid=Student.objects.get(sloginid=request.GET.get('sloginid')))
        resume.save()
        # 返回前端response
        response['msg'] = 'success'
        response['error_num'] = 0
    # 处理异常
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 获取学生的初始兴趣
# 兴趣字段需要在新建学生时进行初始化！！！然后以空格分割的字符串形式存入数据库
@require_http_methods(["GET"])
def get_initial_interest(request):
    response = {}
    try:
        # 找到学生并且初始化兴趣
        sloginid_input = request.GET.get('sloginid')
        interest_input = request.GET.getlist('interest')
        student = Student.objects.get(sloginid=sloginid_input)
        for i in range(MAX_INTEREST_LENGTH):
            if str(i) in interest_input:
                student.interest = student.interest + "50" + " "
            else:
                student.interest = student.interest + "0" + " "
        student.save()
        # 返回前端response
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
        # 找到学生并对比密码
        sloginid_input = request.GET.get('sloginid')
        spassword_input = request.GET.get('spassword')
        spassword_db = Student.objects.get(sloginid=sloginid_input)
        if spassword_input == spassword_db.spassword:
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
                          ctel=request.GET.get('ctel'), caddress=request.GET.get('caddress'),
                          industry="")
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
        if cpassword_input == cpassword_db.cpassword:
            response['msg'] = 'success'
            response['error_num'] = 0
        else:
            response['msg'] = "password wrong"
            response['error_num'] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 2
    return JsonResponse(response)


# 填写公司信息
# @todo 1st function to be done
@require_http_methods(["GET"])
def add_companyForm(request):
    response = {}
    try:
        company = Company.objects.get(cname=request.GET.get('cname'))
        company.scale = request.GET.get('scale')
        company.industry = request.GET.get('industry')
        response['msg'] = 'success'
        response['error_num'] = 0

    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 添加招聘信息
# @todo 2nd function to be done
@require_http_methods(["GET"])
def add_job(request):
    response = {}
    try:
        # jobinfo = json.loads(request.GET.get('jobinfo'))
        job = Job(jobid=genRandomString(), jobinfo=request.GET.get('jobinfo'),
                  company_companyid=Company.objects.get(cloginid=request.GET.get('companyid')),
                  tag=request.GET.get('jobtag'), jname=request.GET.get('jname'),
                  jobpop=0, salary=request.GET.get('salary'), jplace=request.GET.get('jplace'))
        job.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 查看招聘信息
# @todo chage by view time
@require_http_methods(["GET"])
def show_job(request):
    response = {}
    global max_pop
    try:
        sloginid_input = request.GET.get('sloginid')
        jobtag = request.GET.get('jobtag')
        # 更改招聘信息热度
        job = Job.objects.get(jname=request.GET.get('jname'))
        job.jobpop += 1
        if job.jobpop > max_pop:
            max_pop = job.jobpop
        response['jname'] = job.jname
        response['salary'] = job.salary
        response['jplace'] = job.jplace
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 添加简历
# @todo 添加最后两拦信息
@require_http_methods(["GET"])
def add_resume(request):
    response = {}
    try:
        initial_resume = Resume.objects.get(
            student_studentid=Student.objects.get(sloginid=request.GET.get('studentid')))
        initial_resume.delete()
        student = Student.objects.get(sloginid=request.GET.get('studentid'))
        resume = Resume(resumeid=genRandomString(10),
                        student_studentid=student,
                        sname=student.sname, sgrade=student.sgrade,
                        sschool=student.sschool,
                        smajor=student.smajor, skillinfo=request.GET.get('skillinfo'),
                        selfintro=request.GET.get('selfintro'), detail=request.GET.get('detail'),
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
                        selfintro=request.GET.get('selfintro'), detail=request.GET.get('detail'),
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
        resume_db = Resume.objects.get(student_studentid=Student.objects.get(sloginid=sloginid_input))
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
        response['detail'] = resume_db.detail
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 推荐招聘信息
@require_http_methods(["GET"])
def get_recommend_jobs(request):
    response = {}
    try:
        sloginid_input = request.GET.get('sloginid')
        jobs = recommendation_by_tag(sloginid_input)
        # jobs = {}
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


# @todo change weight of interest when click on the job


# this function is a test case for recommendation by pop
def recommendation_by_jobpop():
    s = []
    job_list = []
    for i in Job.objects.all():
        job_list.append(i.jobid, i.jobpop)

    for i in range(len(job_list)):
        for j in range(0, len(job_list) - i - 1):
            if job_list[j].jobpop < job_list[j + 1].jobpop:
                job_list[j], job_list[j + 1] = job_list[j + 1], job_list[j]

    while (len(s) < 2):
        x = random.randint(0, 99)
        if job_list[x].jobid not in s:
            s.append(job_list[x].jobid)
    # s中存储了推荐招聘信息的id，查询并返回招聘信息内容即可
    return s


# this function is a test case for recommendation by tag
# 已经可以将存储的兴趣列表转化为list
def recommendation_by_tag(stdid):
    student = Student.objects.get(sloginid=stdid)
    tag = student.interest.split()
    # print(tag)

    # 需要将json格式的数组读取到这个数组里
    # reply：没有json文件了，tag是兴趣的list
    arr = [i for i in range(len(tag))]

    for i in range(len(tag)):
        for j in range(0, len(tag) - i - 1):
            if tag[j] < tag[j + 1]:
                tag[j], tag[j + 1] = tag[j + 1], tag[j]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    s = []
    while (len(s) < 3):
        x = random.randint(0, 9)
        if arr[x] not in s:
            s.append(arr[x])

    jobid_list = []

    for i in range(3):
        job_list = []
        for j in Job.objects.filter(tag=arr[i]):
            job_list.append(j.jobid, j.jobpop)

        for k in range(len(job_list)):
            for l in range(0, len(job_list) - k - 1):
                if job_list[l].jobpop < job_list[l + 1].jobpop:
                    job_list[l], job_list[l + 1] = job_list[l + 1], job_list[l]

        x = random.randint(0, 19)
        jobid_list.append(job_list[x].jobid)
        # jobid_list中保存了根据tag选出的3个招聘信息的id，返回根据id查询得到的招聘信息即可
    return jobid_list


# this function is a test case for recommendation by pop
def recommendation_by_seminarpop():
    s = []
    seminar_list = []
    for i in Seminar.objects.all():
        seminar_list.append(i.seminarid, i.seminarpop)

    for i in range(len(seminar_list)):
        for j in range(0, len(seminar_list) - i - 1):
            if seminar_list[j].seminarpop < seminar_list[j + 1].seminarpop:
                seminar_list[j], seminar_list[j + 1] = seminar_list[j + 1], seminar_list[j]

    while (len(s) < 2):
        x = random.randint(0, 99)
        if seminar_list[x].seminarid not in s:
            s.append(seminar_list[x].seminarid)
    # s中存储了推荐宣讲会的id，查询并返回宣讲会内容即可
    return s


def key_word_recommendation():
    key_word = Enum('name', ('销售', '客服', '人事', '餐饮', '旅游',
                             '物业', '健身', '房产中介', '家政', '交通服务', '财务', '法律',
                             '翻译', '编辑', '计算机', '投资', '证券', '医疗', '服装', '制药', '公关'))
    s = []
    while (len(s) < 3):
        x = random.randint(1, 21)
        if key_word(x).name not in s:
            s.append(key_word(x).name)
    return s
