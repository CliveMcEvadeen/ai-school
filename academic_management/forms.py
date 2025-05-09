from django import forms
from .models import Curriculum, Syllabus, Timetable, LessonPlan, Resource

class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ['course', 'title', 'description']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ['curriculum', 'subject', 'content']
        widgets = {
            'curriculum': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['course', 'session', 'day_of_week', 'start_time', 'end_time', 'subject']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-select'}),
            'session': forms.Select(attrs={'class': 'form-select'}),
            'day_of_week': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
        }

class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = ['subject', 'title', 'objectives', 'activities', 'resources']
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'objectives': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'activities': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'resources': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['lesson_plan', 'title', 'file', 'description']
        widgets = {
            'lesson_plan': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
