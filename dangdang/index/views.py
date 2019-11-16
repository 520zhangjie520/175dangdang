from django.shortcuts import render
from index.models import BookClass,TBook

# Create your views here.
#==================主页面渲染=================
def index(request):
    category=BookClass.objects.filter(boo_id=None)  # 一级分类
    category_c=BookClass.objects.all()              # 全部分类
    newbook=TBook.objects.all().order_by('ground_time')[0:8]   # 最新上架
    managerbook=TBook.objects.all().order_by('customer_rat')[0:10]   # 主编推荐
    salesbook=TBook.objects.all().order_by('sales_vol')[0:5]   # 新书热卖榜
    salesbook_1=TBook.objects.all().order_by('sales_vol')[0:10]  # 新书热卖榜（主编推荐）
    return render(request,'index.html',{'category':category,'category_c':category_c,'newbook':newbook,'managerbook':managerbook,'salesbook':salesbook,'salesbook_1':salesbook_1})