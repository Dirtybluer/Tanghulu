import json
from django.shortcuts import render
from .models import User
from django.http import HttpResponse


def post_user_info(request):
    data = json.loads(request.body)
    User(
        stu_id=data.get('stu_id'),
        user_name=data.get('user_name'),
        password=data.get('password'),
        gender=data.get('gender'),
        grade=data.get('grade'),
        campus=data.get('campus'),
        school=data.get('school'),
        phone_num=data.get('phone_num'),
    ).save()
    return HttpResponse('OK')
