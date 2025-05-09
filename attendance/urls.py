from django.urls import path
from . import views

urlpatterns = [
    # Attendance URLs
    path('add/', views.add_attendance, name='add_attendance'),
    path('manage/', views.manage_attendance, name='manage_attendance'),
    path('edit/<int:attendance_id>/', views.edit_attendance, name='edit_attendance'),
    path('delete/<int:attendance_id>/', views.delete_attendance, name='delete_attendance'),

    # Attendance Report URLs
    path('report/add/', views.add_attendance_report, name='add_attendance_report'),
    path('report/manage/', views.manage_attendance_report, name='manage_attendance_report'),
    path('report/edit/<int:report_id>/', views.edit_attendance_report, name='edit_attendance_report'),
    path('report/delete/<int:report_id>/', views.delete_attendance_report, name='delete_attendance_report'),
]
