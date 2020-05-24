from django.shortcuts import render
from .models import User
from django.http import HttpResponse


def post_user_info(request):
    User(
        stu_id=request.POST.get('stu_id'),
        user_name=request.POST.get('user_name'),
        password=request.POST.get('password'),
        gender=request.POST.get('gender'),
        grade=request.POST.get('grade'),
        campus=request.POST.get('campus'),
        school=request.POST.get('school'),
        phone_num=request.POST.get('phone_num'),
    ).save()
    return HttpResponse('OK')
