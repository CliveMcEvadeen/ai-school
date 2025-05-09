from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import Exam, Quiz, Assignment, Gradebook, ReportCard, ExamTimetable, StudentResult, ExamDocument, ExamFeedback
from .forms import ExamForm, QuizForm, AssignmentForm, GradebookForm, ReportCardForm, ExamTimetableForm, ExamDocumentForm, ExamFeedbackForm


# Exam Views
def add_exam(request):
    form = ExamForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Exam'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Exam added successfully")
            return redirect(reverse('add_exam'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/add_exam.html', context)


def manage_exam(request):
    exams = Exam.objects.all()
    context = {'exams': exams, 'page_title': 'Manage Exams'}
    return render(request, 'results/manage_exam.html', context)


def edit_exam(request, exam_id):
    instance = get_object_or_404(Exam, id=exam_id)
    form = ExamForm(request.POST or None, instance=instance)
    context = {'form': form, 'exam_id': exam_id, 'page_title': 'Edit Exam'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Exam updated successfully")
            return redirect(reverse('manage_exam'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/edit_exam.html', context)


def delete_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    exam.delete()
    messages.success(request, "Exam deleted successfully")
    return redirect(reverse('manage_exam'))


# Exam Document Views
def manage_exam_documents(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    documents = exam.documents.all()
    context = {'exam': exam, 'documents': documents, 'page_title': 'Manage Exam Documents'}
    return render(request, 'results/manage_exam_documents.html', context)


def add_exam_document(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == 'POST':
        form = ExamDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.exam = exam
            document.save()
            messages.success(request, 'Document uploaded successfully.')
            return redirect(reverse('manage_exam_documents', args=[exam.id]))
    else:
        form = ExamDocumentForm(initial={'exam': exam})
    context = {'form': form, 'exam': exam, 'page_title': 'Add Exam Document'}
    return render(request, 'results/add_exam_document.html', context)


def edit_exam_document(request, document_id):
    document = get_object_or_404(ExamDocument, id=document_id)
    if request.method == 'POST':
        form = ExamDocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            messages.success(request, 'Document updated successfully.')
            return redirect(reverse('manage_exam_documents', args=[document.exam.id]))
    else:
        form = ExamDocumentForm(instance=document)
    context = {'form': form, 'exam': document.exam, 'page_title': 'Edit Exam Document'}
    return render(request, 'results/edit_exam_document.html', context)


def delete_exam_document(request, document_id):
    document = get_object_or_404(ExamDocument, id=document_id)
    exam_id = document.exam.id
    document.delete()
    messages.success(request, 'Document deleted successfully.')
    return redirect(reverse('manage_exam_documents', args=[exam_id]))


# Exam Feedback Views
def add_exam_feedback(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == 'POST':
        form = ExamFeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.exam = exam
            feedback.student = request.user.student  # Assuming logged in user is a student
            feedback.save()
            messages.success(request, 'Feedback submitted successfully.')
            return redirect(reverse('view_exam_feedback', args=[exam.id]))
    else:
        form = ExamFeedbackForm(initial={'exam': exam})
    context = {'form': form, 'exam': exam, 'page_title': 'Add Exam Feedback'}
    return render(request, 'results/add_exam_feedback.html', context)


def view_exam_feedback(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    feedbacks = exam.feedbacks.all()
    context = {'exam': exam, 'feedbacks': feedbacks, 'page_title': 'View Exam Feedback'}
    return render(request, 'results/view_exam_feedback.html', context)


# Quiz Views
def add_quiz(request):
    form = QuizForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Quiz'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Quiz added successfully")
            return redirect(reverse('add_quiz'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/add_quiz.html', context)


def manage_quiz(request):
    quizzes = Quiz.objects.all()
    context = {'quizzes': quizzes, 'page_title': 'Manage Quizzes'}
    return render(request, 'results/manage_quiz.html', context)


def edit_quiz(request, quiz_id):
    instance = get_object_or_404(Quiz, id=quiz_id)
    form = QuizForm(request.POST or None, instance=instance)
    context = {'form': form, 'quiz_id': quiz_id, 'page_title': 'Edit Quiz'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Quiz updated successfully")
            return redirect(reverse('manage_quiz'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/edit_quiz.html', context)


def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    messages.success(request, "Quiz deleted successfully")
    return redirect(reverse('manage_quiz'))


# Assignment Views
def add_assignment(request):
    form = AssignmentForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Assignment'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Assignment added successfully")
            return redirect(reverse('add_assignment'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/add_assignment.html', context)


def manage_assignment(request):
    assignments = Assignment.objects.all()
    context = {'assignments': assignments, 'page_title': 'Manage Assignments'}
    return render(request, 'results/manage_assignment.html', context)


def edit_assignment(request, assignment_id):
    instance = get_object_or_404(Assignment, id=assignment_id)
    form = AssignmentForm(request.POST or None, instance=instance)
    context = {'form': form, 'assignment_id': assignment_id, 'page_title': 'Edit Assignment'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Assignment updated successfully")
            return redirect(reverse('manage_assignment'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/edit_assignment.html', context)


def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    assignment.delete()
    messages.success(request, "Assignment deleted successfully")
    return redirect(reverse('manage_assignment'))


# Gradebook Views
def add_gradebook(request):
    form = GradebookForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Gradebook Entry'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Gradebook entry added successfully")
            return redirect(reverse('add_gradebook'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/add_gradebook.html', context)


def manage_gradebook(request):
    gradebooks = Gradebook.objects.all()
    context = {'gradebooks': gradebooks, 'page_title': 'Manage Gradebook'}
    return render(request, 'results/manage_gradebook.html', context)


def edit_gradebook(request, gradebook_id):
    instance = get_object_or_404(Gradebook, id=gradebook_id)
    form = GradebookForm(request.POST or None, instance=instance)
    context = {'form': form, 'gradebook_id': gradebook_id, 'page_title': 'Edit Gradebook Entry'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Gradebook entry updated successfully")
            return redirect(reverse('manage_gradebook'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/edit_gradebook.html', context)


def delete_gradebook(request, gradebook_id):
    gradebook = get_object_or_404(Gradebook, id=gradebook_id)
    gradebook.delete()
    messages.success(request, "Gradebook entry deleted successfully")
    return redirect(reverse('manage_gradebook'))


# ReportCard Views
def add_report_card(request):
    form = ReportCardForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Report Card'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Report card added successfully")
            return redirect(reverse('add_report_card'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/add_report_card.html', context)


def manage_report_card(request):
    report_cards = ReportCard.objects.all()
    context = {'report_cards': report_cards, 'page_title': 'Manage Report Cards'}
    return render(request, 'results/manage_report_card.html', context)


def edit_report_card(request, report_card_id):
    instance = get_object_or_404(ReportCard, id=report_card_id)
    form = ReportCardForm(request.POST or None, instance=instance)
    context = {'form': form, 'report_card_id': report_card_id, 'page_title': 'Edit Report Card'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Report card updated successfully")
            return redirect(reverse('manage_report_card'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/edit_report_card.html', context)


def delete_report_card(request, report_card_id):
    report_card = get_object_or_404(ReportCard, id=report_card_id)
    report_card.delete()
    messages.success(request, "Report card deleted successfully")
    return redirect(reverse('manage_report_card'))


# ExamTimetable Views
def add_exam_timetable(request):
    form = ExamTimetableForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Exam Timetable'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Exam timetable added successfully")
            return redirect(reverse('add_exam_timetable'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/add_exam_timetable.html', context)


def manage_exam_timetable(request):
    exam_timetables = ExamTimetable.objects.all()
    context = {'exam_timetables': exam_timetables, 'page_title': 'Manage Exam Timetables'}
    return render(request, 'results/manage_exam_timetable.html', context)


def edit_exam_timetable(request, exam_timetable_id):
    instance = get_object_or_404(ExamTimetable, id=exam_timetable_id)
    form = ExamTimetableForm(request.POST or None, instance=instance)
    context = {'form': form, 'exam_timetable_id': exam_timetable_id, 'page_title': 'Edit Exam Timetable'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Exam timetable updated successfully")
            return redirect(reverse('manage_exam_timetable'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'results/edit_exam_timetable.html', context)


def delete_exam_timetable(request, exam_timetable_id):
    exam_timetable = get_object_or_404(ExamTimetable, id=exam_timetable_id)
    exam_timetable.delete()
    messages.success(request, "Exam timetable deleted successfully")
    return redirect(reverse('manage_exam_timetable'))
