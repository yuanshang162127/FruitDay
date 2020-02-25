from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index_views(request):
    return render(request,'index.html')

def login_views(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html',locals())

def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        uphone = request.POST.get('uphone')
        #验证uphone在数据库中是否存在
        users=Users.objects.filter(uphone=uphone)
        if users:
            return render(request,'register.html',{'errMsg':'电话号码已经存在'})
        #继续接收其他数据
        upwd = request.POST.get('upwd')
        uname = request.POST.get('uname')
        uemail = request.POST.get('uemail')
        Users.objects.create(
            uphone=uphone,
            upwd = upwd,
            uname = uname,
            uemail = uemail
        )
        return redirect('/')



def register01_views(request):
    Users.objects.create(
        uphone = '13912345678',
        upwd = '123456',
        uname = '隔壁老王',
        uemail = 'wangwc@163.com'
    )
    return HttpResponse("注册成功")

