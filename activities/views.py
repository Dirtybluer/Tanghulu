from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity
from users.models import User
from datetime import datetime


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
