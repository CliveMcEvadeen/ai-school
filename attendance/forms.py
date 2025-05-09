from django import forms
from .models import Attendance, AttendanceReport

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['session', 'subject', 'date']
        widgets = {
            'session': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class AttendanceReportForm(forms.ModelForm):
    class Meta:
        model = AttendanceReport
        fields = ['student', 'attendance', 'status']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'attendance': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
