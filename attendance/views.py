from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import Attendance, AttendanceReport
from .forms import AttendanceForm, AttendanceReportForm

# Attendance Views
def add_attendance(request):
    form = AttendanceForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Attendance'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Attendance added successfully")
            return redirect(reverse('add_attendance'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'attendance/add_attendance.html', context)


def manage_attendance(request):
    attendances = Attendance.objects.all()
    context = {'attendances': attendances, 'page_title': 'Manage Attendance'}
    return render(request, 'attendance/manage_attendance.html', context)


def edit_attendance(request, attendance_id):
    instance = get_object_or_404(Attendance, id=attendance_id)
    form = AttendanceForm(request.POST or None, instance=instance)
    context = {'form': form, 'attendance_id': attendance_id, 'page_title': 'Edit Attendance'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Attendance updated successfully")
            return redirect(reverse('manage_attendance'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'attendance/edit_attendance.html', context)


def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    attendance.delete()
    messages.success(request, "Attendance deleted successfully")
    return redirect(reverse('manage_attendance'))


# Attendance Report Views
def add_attendance_report(request):
    form = AttendanceReportForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Attendance Report'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Attendance report added successfully")
            return redirect(reverse('add_attendance_report'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'attendance/add_attendance_report.html', context)


def manage_attendance_report(request):
    reports = AttendanceReport.objects.all()
    context = {'reports': reports, 'page_title': 'Manage Attendance Reports'}
    return render(request, 'attendance/manage_attendance_report.html', context)


def edit_attendance_report(request, report_id):
    instance = get_object_or_404(AttendanceReport, id=report_id)
    form = AttendanceReportForm(request.POST or None, instance=instance)
    context = {'form': form, 'report_id': report_id, 'page_title': 'Edit Attendance Report'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Attendance report updated successfully")
            return redirect(reverse('manage_attendance_report'))
        else:
            messages.error(request, "Please correct the errors below")
    return render(request, 'attendance/edit_attendance_report.html', context)


def delete_attendance_report(request, report_id):
    report = get_object_or_404(AttendanceReport, id=report_id)
    report.delete()
    messages.success(request, "Attendance report deleted successfully")
    return redirect(reverse('manage_attendance_report'))
