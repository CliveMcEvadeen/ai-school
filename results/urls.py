from django.urls import path
from . import views

urlpatterns = [
    # Exam URLs
    path('exam/add/', views.add_exam, name='add_exam'),
    path('exam/manage/', views.manage_exam, name='manage_exam'),
    path('exam/edit/<int:exam_id>/', views.edit_exam, name='edit_exam'),
    path('exam/delete/<int:exam_id>/', views.delete_exam, name='delete_exam'),

    # Exam Document URLs
    path('exam/documents/manage/<int:exam_id>/', views.manage_exam_documents, name='manage_exam_documents'),
    path('exam/documents/add/<int:exam_id>/', views.add_exam_document, name='add_exam_document'),
    path('exam/documents/edit/<int:document_id>/', views.edit_exam_document, name='edit_exam_document'),
    path('exam/documents/delete/<int:document_id>/', views.delete_exam_document, name='delete_exam_document'),

    # Exam Feedback URLs
    path('exam/feedback/add/<int:exam_id>/', views.add_exam_feedback, name='add_exam_feedback'),
    path('exam/feedback/view/<int:exam_id>/', views.view_exam_feedback, name='view_exam_feedback'),

    # Quiz URLs
    path('quiz/add/', views.add_quiz, name='add_quiz'),
    path('quiz/manage/', views.manage_quiz, name='manage_quiz'),
    path('quiz/edit/<int:quiz_id>/', views.edit_quiz, name='edit_quiz'),
    path('quiz/delete/<int:quiz_id>/', views.delete_quiz, name='delete_quiz'),

    # Assignment URLs
    path('assignment/add/', views.add_assignment, name='add_assignment'),
    path('assignment/manage/', views.manage_assignment, name='manage_assignment'),
    path('assignment/edit/<int:assignment_id>/', views.edit_assignment, name='edit_assignment'),
    path('assignment/delete/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),

    # Gradebook URLs
    path('gradebook/add/', views.add_gradebook, name='add_gradebook'),
    path('gradebook/manage/', views.manage_gradebook, name='manage_gradebook'),
    path('gradebook/edit/<int:gradebook_id>/', views.edit_gradebook, name='edit_gradebook'),
    path('gradebook/delete/<int:gradebook_id>/', views.delete_gradebook, name='delete_gradebook'),

    # ReportCard URLs
    path('report_card/add/', views.add_report_card, name='add_report_card'),
    path('report_card/manage/', views.manage_report_card, name='manage_report_card'),
    path('report_card/edit/<int:report_card_id>/', views.edit_report_card, name='edit_report_card'),
    path('report_card/delete/<int:report_card_id>/', views.delete_report_card, name='delete_report_card'),

    # ExamTimetable URLs
    path('exam_timetable/add/', views.add_exam_timetable, name='add_exam_timetable'),
    path('exam_timetable/manage/', views.manage_exam_timetable, name='manage_exam_timetable'),
    path('exam_timetable/edit/<int:exam_timetable_id>/', views.edit_exam_timetable, name='edit_exam_timetable'),
    path('exam_timetable/delete/<int:exam_timetable_id>/', views.delete_exam_timetable, name='delete_exam_timetable'),
]
