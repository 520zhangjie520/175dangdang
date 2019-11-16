from django.urls import path
from index import views
urlpatterns=[
    path('index/',views.index,name='index')
]