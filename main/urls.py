from django.urls import path
from django.conf.urls import handler404
from .views import ( 
    HomePageView, GroupsPageView ,TeachersPageView, 
    StudentPageView, StudentDetailView, TeacherDetailView, 
    GroupDetailView, Search_view, Page404View,
)
handler404 = Page404View


urlpatterns = [
    path('', HomePageView, name='home'),
    path('group_list/', GroupsPageView, name='group_list'),
    path('teacher_list/', TeachersPageView, name = 'teacher_list'),
    path('student_list/', StudentPageView, name='student_list'),
    path('student_detail/<str:id>/', StudentDetailView, name='student_detail'),
    path('teacher_detail/<str:id>/', TeacherDetailView, name = 'teacher_detail'),
    path('group_detail/<str:id>/', GroupDetailView, name='group_detail'),
    path('search/', Search_view, name='search'),

]
