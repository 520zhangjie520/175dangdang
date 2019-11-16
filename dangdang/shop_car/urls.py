from django.urls import path
from shop_car import views

app_name='shop_car'
urlpatterns=[
    path('shop_car/',views.shop_car,name='shop_car'),
    path('a_d_u_car/',views.a_d_u_car,name='a_d_u_car'),
    path('show_shop/',views.show_shop,name='show_shop'),
    path('re_del/',views.re_del,name='re_del'),
    path('re_dellogic/',views.re_dellogic,name='re_dellogic'),
    path('re_savelogic/',views.re_savelogic,name='re_savelogic'),
]