from django.urls import path
from . import views

urlpatterns = [
    # Curriculum URLs
    path('curriculum/add/', views.add_curriculum, name='add_curriculum'),
    path('curriculum/manage/', views.manage_curriculum, name='manage_curriculum'),
    path('curriculum/edit/<int:curriculum_id>/', views.edit_curriculum, name='edit_curriculum'),
    path('curriculum/delete/<int:curriculum_id>/', views.delete_curriculum, name='delete_curriculum'),

    # Syllabus URLs
    path('syllabus/add/', views.add_syllabus, name='add_syllabus'),
    path('syllabus/manage/', views.manage_syllabus, name='manage_syllabus'),
    path('syllabus/edit/<int:syllabus_id>/', views.edit_syllabus, name='edit_syllabus'),
    path('syllabus/delete/<int:syllabus_id>/', views.delete_syllabus, name='delete_syllabus'),

    # Timetable URLs
    path('timetable/add/', views.add_timetable, name='add_timetable'),
    path('timetable/manage/', views.manage_timetable, name='manage_timetable'),
    path('timetable/edit/<int:timetable_id>/', views.edit_timetable, name='edit_timetable'),
    path('timetable/delete/<int:timetable_id>/', views.delete_timetable, name='delete_timetable'),

    # LessonPlan URLs
    path('lesson_plan/add/', views.add_lesson_plan, name='add_lesson_plan'),
    path('lesson_plan/manage/', views.manage_lesson_plan, name='manage_lesson_plan'),
    path('lesson_plan/edit/<int:lesson_plan_id>/', views.edit_lesson_plan, name='edit_lesson_plan'),
    path('lesson_plan/delete/<int:lesson_plan_id>/', views.delete_lesson_plan, name='delete_lesson_plan'),

    # Resource URLs
    path('resource/add/', views.add_resource, name='add_resource'),
    path('resource/manage/', views.manage_resource, name='manage_resource'),
    path('resource/edit/<int:resource_id>/', views.edit_resource, name='edit_resource'),
    path('resource/delete/<int:resource_id>/', views.delete_resource, name='delete_resource'),
]
