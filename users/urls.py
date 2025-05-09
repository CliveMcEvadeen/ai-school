from django.urls import path
from . import views

urlpatterns = [
    path('add_staff/', views.add_staff, name='add_staff'),
    path('add_student/', views.add_student, name='add_student'),
    path('manage_staff/', views.manage_staff, name='manage_staff'),
    path('manage_student/', views.manage_student, name='manage_student'),
    path('edit_staff/<int:staff_id>/', views.edit_staff, name='edit_staff'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete_staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('staff_view_profile/', views.staff_view_profile, name='staff_view_profile'),
    path('student_view_profile/', views.student_view_profile, name='student_view_profile'),
]
