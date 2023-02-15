
from django.contrib import admin
from django.urls import path
from app.views import Home,ViewAttend,AddStudent,TakeAttendence

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('viewattend',ViewAttend,name='viewattendenct'),
    path('addstd',AddStudent,name='addstudent'),
    path('attendence',TakeAttendence,name='takeattendence')
]
