# login required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from functools import wraps

from book_site import settings


def check_login(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if  request.user.role != 'Admin':
                return HttpResponse('siz admin emassiz')
        return view_func(request, *args, **kwargs)
    return wrapper


def send_sample_mail(request):

    send_mail(
        subject="Send_mail",

        message="Emailga xabar yuborishni urganyapman",

        from_email=settings.EMAIL_HOST_USER,

        recipient_list=["shohjahonsobirjonov2007@gmail.com",],

        fail_silently=False,
    )
    return HttpResponse('emailingizga xabar yuborildi')

