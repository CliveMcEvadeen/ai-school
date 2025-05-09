from django.urls import path
from . import views

urlpatterns = [
    path('view_staff_leave/', views.view_staff_leave, name='view_staff_leave'),
    path('view_student_leave/', views.view_student_leave, name='view_student_leave'),
    path('student_apply_leave/', views.student_apply_leave, name='student_apply_leave'),
]
