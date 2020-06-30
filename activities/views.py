from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity
from users.models import User
from datetime import datetime
import json


def post_activity(request):
    Activity(
        name=request.POST.get('name'),
        category=request.POST.get('category'),
        address=request.POST.get('address'),
        male_wanted=request.POST.get('male_wanted'),
        female_wanted=request.POST.get('female_wanted'),
        start_time=datetime.strptime(request.POST.get('start_time'), "%Y-%m-%d %H:%M"),
        end_time=datetime.strptime(request.POST.get('end_time'), "%Y-%m-%d %H:%M"),
        publisher=User.objects.get(stu_id=request.POST.get('publisher')),
        description=request.POST.get('description')
        ).save()
    return HttpResponse('OK')

def get_activity_list(request):
    activity_list = []
    activity_info = {
            "name": "打篮球",
            "category": "SP",
            "start_time": "2020-5-21 13:14",
            "end_time": "2020-5-21 13:14",
            "adress": "巴普特大学操场",
            "male_wanted": 0,
            "female_wanted": 100,
            "publisher": "杨哥",
            "description": "仅限女生哦"
            }
    for i in range(10):
        activity_list.append(activity_info)
   
    return JsonResponse(activity_list, safe=False)
