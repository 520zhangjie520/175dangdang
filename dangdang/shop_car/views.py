from django.http import HttpResponse
from django.shortcuts import render
from index.models import TShop,TUser,TBook
from dangdang.car import Car, Sql
import re

# Create your views here.
#============购物车页面渲染=========
def shop_car(request):

    return render(request,'car.html')
#============购物车de/增/删/改============
def a_d_u_car(request):
    lo=request.session.get('login')
    flag=request.GET.get('flag')
    id = request.GET.get('id')
    number = request.GET.get('number','1')
    print('=============================================================================')
    print(flag,id,number)
    rule = '([1-9]{1,3})$'
    # rule = '/^(?=.*?[1-9]).{1,3}$/'
    if re.match(rule,number):
        pass
    else:
        number=1
    car_inf=request.session.get('car_inf')
    print(car_inf)
    if car_inf:
        pass
    else:
        car_inf=Car()
    #-----增-----
    if flag=='1':
        car_inf.add(id,int(number))
        if lo:
            username = request.session.get('username')
            Sql().add(username,car_inf)
        request.session['car_inf'] = car_inf
        return HttpResponse('1')
    #-----改-----
    elif flag=='3':
        car_inf.update(id,int(number))
        if lo:
            username=request.session.get('username')
            user=TUser.objects.get(username=username)
            Sql().update(id,int(number),car_inf,user.id)
        request.session['car_inf'] = car_inf
        return HttpResponse('1')
#==============已购商品展示==============
def show_shop(request):
    car_inf=request.session.get('car_inf')
    if car_inf:
        if car_inf.car_item:
            flag=1
        else:
            flag=0
    else:
        flag=0
    return render(request,'show_shop.html',{'car_inf':car_inf,'flag':flag})
#============删除恢复=================
#-----------删除恢复页面渲染-----------
def re_del(request):
    car_re=request.session.get('car_re')
    if car_re:
        if car_re.car_item:
            flag=1
        else:
            flag=0
    else:
        flag=0
    return render(request,'del_shop.html',{'car_re':car_re,'flag':flag})
#-----------删除逻辑---------
def re_dellogic(request):
    lo=request.session.get('login')
    id=request.GET.get('id')
    number=int(request.GET.get('number',1))
    car_inf=request.session.get('car_inf')
    car_re=request.session.get('car_re')
    if car_re:
       pass
    else:
        car_re=Car()
    car_re.add(id,number)
    car_inf.dele(id)
    if lo:
        username=request.session.get('username')
        user=TUser.objects.get(username=username)
        Sql().dele(user.id,id)
    request.session['car_re']=car_re
    request.session['car_inf']=car_inf
    return HttpResponse('1')

#--------恢复逻辑--------
def re_savelogic(request):
    lo=request.session.get('')
    id=request.GET.get('id')
    number=int(request.GET.get('number',1))
    car_re=request.session.get('car_re')
    car_inf=request.session.get('car_inf')
    car_re.dele(id)
    car_inf.add(id,number)
    if lo:
        username = request.COOKIES.get('username').encode('utf-8').decode('latin-1')
        user = TUser.objects.get(username=username)
        for i in car_inf.car_item:
            TShop.objects.create(user_id=user.id, book_id=id, number=i.number, save_price=i.save_price,all_price=i.all_price)
    request.session['car_re']=car_re
    request.session['car_inf']=car_inf
    return HttpResponse('1')
