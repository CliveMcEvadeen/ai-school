from django.db import models


class Attendance(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    session = models.ForeignKey('courses.Session', on_delete=models.DO_NOTHING)
    subject = models.ForeignKey('courses.Subject', on_delete=models.DO_NOTHING)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AttendanceReport(models.Model):
    tenant = models.ForeignKey('users.Tenant', on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey('users.Student', on_delete=models.DO_NOTHING)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
