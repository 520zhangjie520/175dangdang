from django.urls import path
from log_reg import views

app_name='log_reg'
urlpatterns=[
    path('login/',views.login,name='login'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
    path('regist/',views.regist,name='regist'),
    path('registlogic/',views.registlogic,name='registlogic'),
    path('checkname/',views.checkname,name='checkname'),
    path('captcha/',views.captcha,name='captcha'),
    path('checkcapt/',views.checkcapt,name='checkcapt'),
    path('wel/',views.wel,name='wel'),
    path('out/',views.out,name='out'),
]