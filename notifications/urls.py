from django.urls import path
from . import views

urlpatterns = [
    path('admin_notify_staff/', views.admin_notify_staff, name='admin_notify_staff'),
    path('admin_notify_student/', views.admin_notify_student, name='admin_notify_student'),
    path('send_student_notification/', views.send_student_notification, name='send_student_notification'),
    path('send_staff_notification/', views.send_staff_notification, name='send_staff_notification'),
]
