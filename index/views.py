from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.


def login_views(request):
    # return HttpResponse('login index')
    if request.method=='GET':
        return render(request,'login.html')
    else:
        # 处理用户的登录操作
        uphone=request.POST['uphone']
        upwd=request.POST['upwd']
        users=Users.objects.filter(uphone=uphone,upwd=upwd)
        if users:
            return HttpResponseRedirect('/')
        else:
            errMsg = '用户名或密码输入不正确'
            return render(request,'login.html',locals())


def index_views(request):
    banner=Banner.objects.all()
    return render(request,'index.html',locals())
    # return HttpResponse('main index')


def register_views(request):
    if request.method == 'POST':
        # 如果：ｇｅｔ请求，查看注册页面
        # 如果：ｐｏｓｔ请求，处理提交数据（注册）
        # 接收注册信息，并写入数据库
        uphone=request.POST['uphone']
        users=Users.objects.filter(uphone=uphone)
        if users:
            # 说明用户已存在
            errMsg='电话号码已存在，请重新输入'
            return render(request,'register.html',locals())
        upwd=request.POST['upwd']
        uemail=request.POST['uemail']
        uname=request.POST['uname']
        user=Users.objects.create(uphone=uphone, uname=uname, upwd=upwd, uemail=uemail)
        # user.save()
        return HttpResponseRedirect('/login/')
    elif request.method == 'GET':
        return render(request, 'register.html')
