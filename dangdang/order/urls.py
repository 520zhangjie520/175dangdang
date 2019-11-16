from django.urls import path
from order import views

app_name='order'
urlpatterns=[
    path('show_order/',views.show_order,name='show_order'),
    path('orderlogic/',views.ordelogic,name='orderlogic'),
    path('address/',views.address,name='address'),
]