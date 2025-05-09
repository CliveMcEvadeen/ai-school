from django.urls import path
from . import views

urlpatterns = [
    path('student_feedback_message/', views.student_feedback_message, name='student_feedback_message'),
    path('staff_feedback_message/', views.staff_feedback_message, name='staff_feedback_message'),
    path('student_feedback/', views.student_feedback, name='student_feedback'),
]
