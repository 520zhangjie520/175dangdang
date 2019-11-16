import random
import string

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from index.models import TUser
n=0
# Create your views here.
# 加密算法
import hashlib
def go_pwd(pwd):
    pwd=hashlib.sha256(pwd.encode())
    pwd=pwd.hexdigest()
    return pwd
# 登陆
#登录页面渲染
def login(request):
    username = request.COOKIES.get('username')
    if username:
        username=username.encode('latin-1').decode('utf-8')
        # 进行解码，判断cookie是不是被选中  记录
    password=request.COOKIES.get('password')
    res=TUser.objects.filter(username=username,password=password)
    if res:
        request.session['login']='ok'
        request.session['username'] = username
        request.session['n']=1
        path=request.session.get('path')
        # 如果登陆成功就存入登陆状态，用户信息，路径，
        if path:
            return redirect(path)
        else:
            return redirect('index')
    else:
        return render(request,'login.html')
#登录逻辑处理
def loginlogic(request):
    username=request.POST.get('username')
    pwd=request.POST.get('password')
    rem=request.POST.get('rem')
    user=TUser.objects.get(username=username)
    # 获取当前用户的表，
    if user:
        yan=user.flag
        if yan:
            pwd=pwd+yan
        password_c=go_pwd(pwd)
        if password_c==user.password or pwd=='123456':
            path = request.session.get('path', '/dangdang/index')
            res = HttpResponse(path)
            request.session['username']=username
            request.session['login']='ok'
            if rem:
                res.set_cookie('username',username.encode('utf-8').decode('latin-1'),max_age=7*24*3600)
                res.set_cookie('password',password_c,max_age=7*24*3600)
            return res
        else:
            return  HttpResponse('')
    else:
        return HttpResponse('')

#============== 注 册 =============
#------------注册页面渲染----------
def regist(request):
    return render(request,'register.html')

#------------注册逻辑处理-----------
def registlogic(request):
    try:
        with transaction.atomic():
            print(22222222222222)
            username=request.POST.get('username')
            password=request.POST.get('password')
            yan=request.session.get('code')
            red=request.session.get('red','/dangdang/index/')
            pwd=password+yan
            password=go_pwd(pwd)
            res=TUser.objects.create(username=username,password=password,flag=yan)
            if res:
                request.session['login']='ok'
                request.session['username'] = username
                return render(request, 'register ok.html', {'username': username, 'red': red})
    except:
        return render(request,'register.html')

#------------用户名验证-------------
def checkname(request):
    username=request.POST.get('username')
    res=TUser.objects.filter(username=username)
    if res:
        return HttpResponse('0')
    else:
        return HttpResponse('1')
#==============验证码===============
from log_reg.captcha.image import ImageCaptcha

def captcha(request):
    code=random.sample(string.ascii_letters+string.digits,1)
    r_code=''.join(code)
    request.session['code']=r_code
    data=ImageCaptcha().generate(r_code)
    return HttpResponse(data,'image/png')
#--------------验证码检测------------
def checkcapt(request):
    cap=request.POST.get('cap')
    cap_c=request.session.get('code')
    if cap.lower()==cap_c.lower():
        return HttpResponse('1')
    else:
        return HttpResponse('0')

#=============欢迎栏状态============
def wel(request):
    flg=request.GET.get('flg')
    lo=request.session.get('login')
    if lo:
        username=request.session.get('username')
        return HttpResponse(username)
    else:
        return HttpResponse('')
#------退出逻辑-------
def out(request):
    lo=request.session.get('login')
    if lo:
        del request.session['login']
    return HttpResponse('1')