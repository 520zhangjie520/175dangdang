from django.core.paginator import Paginator
from django.shortcuts import render
from index.models import TBook,BookClass
# Create your views here.
#=================书籍详情页面渲染===============
def bookdetails(requset):
    book_id=requset.GET.get('id',1)
    book_d=TBook.objects.get(id=book_id)
    cate=BookClass.objects.get(id=book_d.class_id)
    id_w=cate.boo_id
    category_list=[{'class_name':cate.class_name,'id':cate.id}]
    print(category_list)
    while id_w:
        cate_add=BookClass.objects.get(id=id_w)
        category_list.append({'class_name':cate_add.class_name,'id':cate_add.id})
        id_w=cate_add.boo_id
    category_list.reverse()
    return render(requset,'Book details.html',{'book_d':book_d,'category_list':category_list,'book_id':book_id})
#================书籍分类展示页面渲染==============
#----------------定义排序函数---------------
def order(flag, query):
    print(flag)
    if flag=='0' or flag==None:
        return query.order_by('id')
    elif flag=='1':
        return query.order_by('sales_vol')
    elif flag == '2':
        return query.order_by('dangdang_price')
    elif flag == '3':
        return query.order_by('publishing_time')
#---------页面渲染---------
def booklist(request):
    category=BookClass.objects.filter(boo_id=None)  # 一级分类
    category_c=BookClass.objects.all()              # 全部分类
    id=request.GET.get('id')
    num=request.GET.get('num',1)
    flag=request.GET.get('flag')
    if flag:
        request.session['flag']=flag
    else:
        flag=request.session.get('flag','0')
    if id:
        request.session['id']=id
    else:
        id=request.session.get('id')
    cate_list=[]
    if id == 't':
        query = TBook.objects.all()
    else:
        cate = BookClass.objects.get(id=id)
        if cate.boo_id:
            cate_list.append({'class_name':cate.class_name,'id':cate.id})
            query = TBook.objects.filter(class_id=id)
            k=cate.boo_id
            while k:
                k_c=BookClass.objects.get(id=k)
                cate_list.append({'class_name':k_c.class_name,'id':k_c.id})
                k=k_c.boo_id
        else:
            cate_list.append({'class_name':cate.class_name,'id':cate.id})
            query_list = []
            cate_c = BookClass.objects.filter(boo_id=cate.id)
            for i in cate_c:
                query_list.append(i.id)
            query = TBook.objects.filter(class_id__in=query_list)
    cate_list.reverse()
    query=order(flag,query)
    pagtor = Paginator(query, per_page=4)
    page = pagtor.page(num)
    return render(request,'booklist.html',{'category':category,'category_c':category_c,'page':page,'cate_list':cate_list,'flag':flag,'book_id':id})
# #-----------------书籍分类逻辑处理-----------------
# def booklistlogic(requst):
#     num=requst.GET.get('num',1)
#     pagtor=Paginator(TBook.objects.all(),per_page=4)  # 构造分页对象
#     page=pagtor.page(num)
#     return render(requst, 'show_shop.html', {'page':page})