import random
import string
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from index.models import TOrder, TAddress, TUser, TShop
# Create your views here.
#======================订单页面渲染======================
def show_order(request):
    if request.session.get('login'):
        user=request.session.get('username')
        user_inf=TUser.objects.get(username=user)
        addr=TAddress.objects.filter(user_id=user_inf.id)
        car_inf=request.session.get('car_inf')
        return render(request,'indent.html',{'addr':addr,'car_inf':car_inf})
    else:
        request.session['red']='/dangdang/show_order'
        return redirect('log_reg:login')
#=====================订单逻辑处理=======================
#-----------订单提交逻辑------------
@csrf_exempt
def ordelogic(request):
    username=request.POST.get('username')
    addr=request.POST.get('address')
    zip=request.POST.get('zipcode')
    tel=request.POST.get('telphone')
    mob=request.POST.get('mobilephone')
    id_flag=request.POST.get('id_flag')
    user=request.session.get('username')
    print(username,addr,zip,tel)
    user_i=TUser.objects.get(username=user)
    if id_flag:
        pass
    else:
        TAddress.objects.create(username=username,address=addr,zipcode=zip,telephone=tel,mobilephone=mob,user_id=user_i.id)
    code = random.sample(string.digits, 10)
    ord_id=''.join(code)
    car_inf=request.session.get('car_inf')
    ord_price=car_inf.all_price
    ord_num=len(car_inf.car_item)
    del request.session['car_inf']
    username=request.session.get('username')
    user=TUser.objects.get(username=username)
    a = TShop.objects.filter(user_id=user.id)
    a.delete()
    return render(request,'indent ok.html',{'ord_id':ord_id,'ord_price':ord_price,'ord_num':ord_num,'username':username})
#-----------地址响应逻辑------------
def address(request):
    try:
        id=request.GET.get('id')
        addr_c=TAddress.objects.get(id=id)
        def mydefault(u):
            if isinstance(u,TAddress):
                addr_c={'username':u.username,'address':u.address,'zipcode':u.zipcode,'tel':u.telephone,'mobile':u.mobilephone}
                return addr_c
        if addr_c:
            return JsonResponse(addr_c,safe=False,json_dumps_params={'default':mydefault})
    except:
        return HttpResponse('1')