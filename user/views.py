from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from .models import Student
import random, string


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
        response['err_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


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


def genRandomString(slen=10):
    return ''.join(random.sample(string.ascii_letters + string.digits, slen))
