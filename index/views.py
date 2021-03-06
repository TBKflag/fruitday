from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.
from .forms import *


def login_views(request):
    # return HttpResponse('login index')
    if request.method=='GET':
        uid = 'uid' in request.COOKIES
        uphone = 'uphone' in request.COOKIES
        se = 'uid' in request.session
        if se:
            return HttpResponseRedirect('/')
        elif uid and uphone:
            # 从ｃｏｏｋｉｅ获取登录信息并保存进ｓｅｓｓｉｏｎ
            uid=request.COOKIES['uid']
            uphone=request.COOKIES['uphone']
            request.session['uid']=uid
            request.session['uphone']=uphone
            return HttpResponseRedirect('/')
        else:
            return render(request,'login.html')
    else:
        # 处理用户的登录操作
        uphone=request.POST['uphone']
        upwd=request.POST['upwd']
        users=Users.objects.filter(uphone=uphone,upwd=upwd)
        if users:
            # 获取用户ＩＤ
            uid=users[0].id
            uphone=users[0].uphone
            request.session['uid']=uid
            request.session['uphone']=uphone
            resp= HttpResponseRedirect('/')
            if 'isRem' in request.POST:
                resp.set_cookie('uid', uid, 60*60*24*366)
                resp.set_cookie('uphone', uphone, 60*60*24*366)
            return resp
        else:
            errMsg = '用户名或密码输入不正确'
            return render(request,'login.html',locals())


def index_views(request):
    banner=Banner.objects.all()
    smallbanners = SmallBanner.objects.all()
    goods=Goods.objects.all()
    uid='uid' in request.COOKIES
    uphone = 'uphone' in request.COOKIES
    se = 'uid' in request.session
    if se:
        uid=request.session['uid']
        uphone=request.session['uphone']
    return render(request,'index.html',locals())



def logout_views(request):
    resp = HttpResponseRedirect('/')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
        resp.delete_cookie('uphone')
    if 'uid' in request.session:
        del request.session['uid']
        del request.session['uphone']
    return resp



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


def gooddetail_views(request,uid):
    uid=uid
    return render(request,'detail.html',locals())


def addcart_views(request,goodid):
    success = 'uid' in request.session
    if success:
        uid = request.session['uid']
        uphone = request.session['uphone']
        obj=Goods.objects.get(id=goodid)

        goods=Cart.objects.create(uphone=uphone,title=obj.title,price=obj.price,pic=obj.picture,num=1)
       
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def subcart_views(request,goodid):
    success = 'uid' in request.session
    if success:
        print(goodid)
        obj = Cart.objects.get(id=goodid)
        obj.delete()
        return HttpResponseRedirect('/cart/')
    else:
        return HttpResponseRedirect('/login/')

def cart_views(request):
    success = 'uid' in request.session
    if success:
        uid = request.session['uid']
        uphone = request.session['uphone']
        goods = Cart.objects.filter(uphone=uphone)
        forms = Cartform()
        return render(request,'cart.html',locals())
    else:
        return HttpResponseRedirect('/login/')

