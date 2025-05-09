from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import Curriculum, Syllabus, Timetable, LessonPlan, Resource
from .forms import CurriculumForm, SyllabusForm, TimetableForm, LessonPlanForm, ResourceForm


# Curriculum Views
def add_curriculum(request):
    form = CurriculumForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Curriculum'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Curriculum added successfully")
            return redirect(reverse('add_curriculum'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'academic_management/add_curriculum.html', context)


def manage_curriculum(request):
    curriculums = Curriculum.objects.all()
    context = {'curriculums': curriculums, 'page_title': 'Manage Curriculum'}
    return render(request, 'academic_management/manage_curriculum.html', context)


def edit_curriculum(request, curriculum_id):
    instance = get_object_or_404(Curriculum, id=curriculum_id)
    form = CurriculumForm(request.POST or None, instance=instance)
    context = {'form': form, 'curriculum_id': curriculum_id, 'page_title': 'Edit Curriculum'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Curriculum updated successfully")
            return redirect(reverse('manage_curriculum'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'academic_management/edit_curriculum.html', context)


def delete_curriculum(request, curriculum_id):
    curriculum = get_object_or_404(Curriculum, id=curriculum_id)
    curriculum.delete()
    messages.success(request, "Curriculum deleted successfully")
    return redirect(reverse('manage_curriculum'))


# Syllabus Views
def add_syllabus(request):
    form = SyllabusForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Syllabus'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Syllabus added successfully")
            return redirect(reverse('add_syllabus'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'academic_management/add_syllabus.html', context)


def manage_syllabus(request):
    syllabuses = Syllabus.objects.all()
    context = {'syllabuses': syllabuses, 'page_title': 'Manage Syllabus'}
    return render(request, 'academic_management/manage_syllabus.html', context)


def edit_syllabus(request, syllabus_id):
    instance = get_object_or_404(Syllabus, id=syllabus_id)
    form = SyllabusForm(request.POST or None, instance=instance)
    context = {'form': form, 'syllabus_id': syllabus_id, 'page_title': 'Edit Syllabus'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Syllabus updated successfully")
            return redirect(reverse('manage_syllabus'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'academic_management/edit_syllabus.html', context)


def delete_syllabus(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, id=syllabus_id)
    syllabus.delete()
    messages.success(request, "Syllabus deleted successfully")
    return redirect(reverse('manage_syllabus'))


# Timetable Views
def add_timetable(request):
    form = TimetableForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Timetable'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Timetable added successfully")
            return redirect(reverse('add_timetable'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'academic_management/add_timetable.html', context)


def manage_timetable(request):
    timetables = Timetable.objects.all()
    context = {'timetables': timetables, 'page_title': 'Manage Timetable'}
    return render(request, 'academic_management/manage_timetable.html', context)


def edit_timetable(request, timetable_id):
    instance = get_object_or_404(Timetable, id=timetable_id)
    form = TimetableForm(request.POST or None, instance=instance)
    context = {'form': form, 'timetable_id': timetable_id, 'page_title': 'Edit Timetable'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Timetable updated successfully")
            return redirect(reverse('manage_timetable'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'academic_management/edit_timetable.html', context)


def delete_timetable(request, timetable_id):
    timetable = get_object_or_404(Timetable, id=timetable_id)
    timetable.delete()
    messages.success(request, "Timetable deleted successfully")
    return redirect(reverse('manage_timetable'))


# LessonPlan Views
def add_lesson_plan(request):
    form = LessonPlanForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Lesson Plan'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Lesson plan added successfully")
            return redirect(reverse('add_lesson_plan'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'academic_management/add_lesson_plan.html', context)


def manage_lesson_plan(request):
    lesson_plans = LessonPlan.objects.all()
    context = {'lesson_plans': lesson_plans, 'page_title': 'Manage Lesson Plans'}
    return render(request, 'academic_management/manage_lesson_plan.html', context)


def edit_lesson_plan(request, lesson_plan_id):
    instance = get_object_or_404(LessonPlan, id=lesson_plan_id)
    form = LessonPlanForm(request.POST or None, instance=instance)
    context = {'form': form, 'lesson_plan_id': lesson_plan_id, 'page_title': 'Edit Lesson Plan'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Lesson plan updated successfully")
            return redirect(reverse('manage_lesson_plan'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'academic_management/edit_lesson_plan.html', context)


def delete_lesson_plan(request, lesson_plan_id):
    lesson_plan = get_object_or_404(LessonPlan, id=lesson_plan_id)
    lesson_plan.delete()
    messages.success(request, "Lesson plan deleted successfully")
    return redirect(reverse('manage_lesson_plan'))


# Resource Views
def add_resource(request):
    form = ResourceForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'page_title': 'Add Resource'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Resource added successfully")
            return redirect(reverse('add_resource'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'academic_management/add_resource.html', context)


def manage_resource(request):
    resources = Resource.objects.all()
    context = {'resources': resources, 'page_title': 'Manage Resources'}
    return render(request, 'academic_management/manage_resource.html', context)


def edit_resource(request, resource_id):
    instance = get_object_or_404(Resource, id=resource_id)
    form = ResourceForm(request.POST or None, request.FILES or None, instance=instance)
    context = {'form': form, 'resource_id': resource_id, 'page_title': 'Edit Resource'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Resource updated successfully")
            return redirect(reverse('manage_resource'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'academic_management/edit_resource.html', context)


def delete_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    resource.delete()
    messages.success(request, "Resource deleted successfully")
    return redirect(reverse('manage_resource'))
