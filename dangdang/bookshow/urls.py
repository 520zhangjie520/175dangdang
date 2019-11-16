from django.urls import path
from bookshow import views
app_name='bookshow'
urlpatterns=[
    path('bookdetails',views.bookdetails,name='bookdetails'),
    path('booklist',views.booklist,name='booklist'),
]