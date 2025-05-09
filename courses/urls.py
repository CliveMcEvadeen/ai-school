from django.urls import path
from . import views

urlpatterns = [
    path('add_course/', views.add_course, name='add_course'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('add_session/', views.add_session, name='add_session'),
    path('manage_course/', views.manage_course, name='manage_course'),
    path('manage_subject/', views.manage_subject, name='manage_subject'),
    path('manage_session/', views.manage_session, name='manage_session'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('edit_subject/<int:subject_id>/', views.edit_subject, name='edit_subject'),
    path('edit_session/<int:session_id>/', views.edit_session, name='edit_session'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('delete_subject/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    path('delete_session/<int:session_id>/', views.delete_session, name='delete_session'),
]
